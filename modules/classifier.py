import pandas as pd
from data.reference_range import REFERENCE_RANGES
from data.aliases import ALIASES
from modules.medical_insights import generate_insight

def find_best_match(test_name: str):
    name = test_name.lower().strip()

    for key in REFERENCE_RANGES:
        if key.lower() == name:
            return key

    for key, aliases in ALIASES.items():
        for a in aliases:
            if a in name or name in a:
                return key

    return None

def classify_value(name, value, gender="general", ref_range=None):

    try:
        value = float(str(value).replace("%", "").strip())
    except:
        return "Unknown", None, None, None

    if ref_range:
        try:
            low, high = float(ref_range[0]), float(ref_range[1])
        except:
            return "Unknown", None, None, None
        source = "pdf"
    else:
        match = find_best_match(name)

        if not match:
            return "Unknown", None, None, None

        ref = REFERENCE_RANGES[match].get(gender) or REFERENCE_RANGES[match].get("general")

        if not ref:
            return "Unknown", None, None, None

        low, high = float(ref["min"]), float(ref["max"])
        source = "db"

    if value < low:
        return "Low", low, high, source
    elif value > high:
        return "High", low, high, source
    else:
        return "Normal", low, high, source

def build_results_table(parsed_values, gender="general"):
    rows = []

    for item in parsed_values:

        status, low, high, source = classify_value(
            item["name"],
            item["value"],
            gender,
            item.get("range")
        )

        test_name = item["name"].strip().title()

        rows.append({
            "Test Name": test_name,
            "Value": item["value"],
            "Unit": item["unit"] if item["unit"] else "-",
            "Status": status,
            "Min": low if low is not None else "-",
            "Max": high if high is not None else "-",
            "Source": source,
            "Insight": generate_insight(test_name, item["value"], status)  # ✅ NEW
        })

    return pd.DataFrame(rows)

def color_status(val):
    styles = {
        "Normal": "color:#16a34a; font-weight:bold;",
        "High": "color:#dc2626; font-weight:bold;",
        "Low": "color:#d97706; font-weight:bold;",
        "Unknown": "color:#6b7280; font-weight:bold;"
    }
    return styles.get(val, "color:black;")