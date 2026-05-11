def generate_insight(test_name, value, status):
    name = test_name.lower()

    if "hemoglobin" in name:
        if status == "Low":
            return "Possible anemia or iron deficiency."
        if status == "High":
            return "Possible dehydration or lung-related stress."

    if "rbc" in name:
        if status == "Low":
            return "Low red blood cells → possible anemia."
        if status == "High":
            return "Possible dehydration or bone marrow overproduction."

    if "wbc" in name:
        if status == "High":
            return "Possible infection or inflammation."
        if status == "Low":
            return "Weak immunity or bone marrow suppression."

    if "platelet" in name:
        if status == "Low":
            return "Risk of bleeding or clotting disorder."
        if status == "High":
            return "Possible inflammation or infection."

    if "glucose" in name or "hba1c" in name:
        if status == "High":
            return "Possible diabetes risk or poor glucose control."
        if status == "Low":
            return "Low blood sugar (hypoglycemia)."

    if "alt" in name or "ast" in name:
        if status == "High":
            return "Possible liver inflammation or damage."

    if "bilirubin" in name:
        if status == "High":
            return "Possible liver or bile duct issue."

    if "creatinine" in name:
        if status == "High":
            return "Possible kidney dysfunction."
        if status == "Low":
            return "Low muscle mass or malnutrition."

    if "urea" in name or "bun" in name:
        if status == "High":
            return "Possible kidney stress or dehydration."

    if "tsh" in name:
        if status == "High":
            return "Possible hypothyroidism."
        if status == "Low":
            return "Possible hyperthyroidism."

    return "Consult a doctor for interpretation."