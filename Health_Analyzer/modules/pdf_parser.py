import pdfplumber
import re
from data.reference_range import REFERENCE_RANGES as _DB_RANGES

def normalize_name(name):
    return re.sub(r"[^a-z]", "", name.lower())

def clean_test_name(name: str) -> str:
    name = str(name).strip()

    name = name.split(":")[0].strip()

    name = re.split(r"-{2,}", name)[0].strip()

    match = re.match(r"^([A-Za-z][A-Za-z0-9 \.\(\)/]*?)(?:\s+[><=]?\s*\d|\s*[><=]\d|$)", name)
    if match:
        name = match.group(1).strip()

    name = name.strip(" .,;/\\-")

    name = re.sub(r"\s{2,}", " ", name)

    if len(name) > 40:
        name = name[:40].rsplit(" ", 1)[0]

    return name.title()


def is_valid_test(name: str) -> bool:
    name = name.lower()

    keywords = [
        "rbc", "r.b.c", "red blood cell",
        "wbc", "white blood cell",
        "hemoglobin", "haemoglobin", "hb",
        "hematocrit", "haematocrit", "hct",
        "mcv", "mch", "mchc", "rdw",
        "neutrophil", "lymphocyte", "monocyte",
        "eosinophil", "basophil",
        "absolute neutrophil", "absolute lymphocyte",
        "absolute monocyte", "absolute eosinophil",
        "absolute basophil",
        "egfr", "gfr", "creatinine", "urea", "bun",
        "glucose", "hba1c", "cholesterol", "triglyceride",
        "ldl", "hdl", "alt", "ast", "alp", "bilirubin",
        "sodium", "potassium", "calcium", "tsh", "t3", "t4",
        "ferritin", "vitamin", "platelet", "plt",
    ]

    return any(k in name for k in keywords)


REFERENCE_RANGES = {}
for key, val in _DB_RANGES.items():
    ref = val.get("general") or val.get("male")
    if ref:
        REFERENCE_RANGES[key.lower()] = (ref["min"], ref["max"])

def get_status(value, ref):
    if not ref:
        return "Unknown"
    low, high = ref
    if value < low:
        return "Low"
    elif value > high:
        return "High"
    return "Normal"


def extract_text(file):
    text, tables = "", []

    with pdfplumber.open(file) as pdf:
        for p in pdf.pages:
            page_text = p.extract_text()
            if page_text:
                text += page_text + "\n"

            page_tables = p.extract_tables()
            if page_tables:
                tables.extend(page_tables)

    return text, tables

def parse_tables(tables):
    results = []

    for table in tables:
        for row in table:
            if not row or len(row) < 2:
                continue

            raw_name = str(row[0]).strip()
            name = clean_test_name(raw_name)

            if not name:
                continue

            value = None
            for cell in row[1:]:
                if cell:
                    match = re.search(r"\d+\.?\d*", str(cell))
                    if match:
                        value = float(match.group())
                        break

            if value is None:
                continue

            ref = None
            for cell in row:
                if cell:
                    match = re.search(r"(\d+\.?\d*)\s*[-–]\s*(\d+\.?\d*)", str(cell))
                    if match:
                        ref = (float(match.group(1)), float(match.group(2)))
                        break

            results.append({
                "name": name,
                "value": value,
                "unit": "",
                "range": ref
            })

    return results

def parse_text(text):
    results = []

    pattern = re.compile(
        r"^(?P<name>[A-Za-z][A-Za-z0-9 \.\(\)/]{1,34}?)\s+"
        r"(?P<value>\d+\.?\d*)\s*"
        r"(?P<unit>%|fL|pg|g/dL|10\^9/L|mmol/L|mg/dL|U/L|mIU/L)?",
        re.IGNORECASE)

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue

        match = pattern.match(line)   #use match
        if not match:
            continue

        try:
            value = float(match.group("value"))
            name  = clean_test_name(match.group("name"))
            unit  = match.group("unit") or ""
        except Exception:
            continue

        if not name:
            continue

        results.append({
            "name": name,
            "value": value,
            "unit": unit,
            "range": None
        })

    return results

def parse_lab_report(file):

    text, tables = extract_text(file)

    table_results = parse_tables(tables)
    text_results  = parse_text(text)

    raw_results = table_results + text_results

    #filter
    filtered = []
    seen = set()

    for r in raw_results:
        name = r["name"]

        if not is_valid_test(name):
            continue

        key = normalize_name(name)
        if key in seen:
            continue

        seen.add(key)
        filtered.append(r)

    for r in filtered:
        key = normalize_name(r["name"])

        if r["range"] is None and key in REFERENCE_RANGES:
            r["range"] = REFERENCE_RANGES[key]

        r["status"] = get_status(r["value"], r["range"])

    return filtered