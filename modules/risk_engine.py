import pandas as pd


RISK_WEIGHTS = {
    "Troponin_I":        10,
    "BNP":               8,
    "CK_MB":             8,
    "Glucose_Fasting":   6,
    "Hba1C":             6,
    "Creatinine":        6,
    "Egfr":              6,
    "Potassium":         6,
    "Sodium":            5,
    "Hemoglobin":        5,
    "WBC":               5,
    "Platelets":         5,
    "TSH":               4,
    "ALT":               4,
    "AST":               4,
    "Total_Bilirubin":   4,
    "LDL":               3,
    "Total_Cholesterol": 3,
    "Triglycerides":     3,
    "CRP":               3,
    "INR":               5,
    "PT":                4,
}

DEFAULT_WEIGHT = 2


def calculate_risk(df: pd.DataFrame) -> tuple[str, str]:
    """
    Returns (risk_level: str, message: str)
    risk_level is one of: 'Low', 'Moderate', 'High'
    """
    if df is None or df.empty:
        return "Unknown", "Not enough data to assess risk."

    abnormal = df[df["Status"].isin(["High", "Low"])]

    if abnormal.empty:
        return "Low", "All values are within normal range. Keep up the healthy lifestyle!"

    score = 0
    flagged_tests = []

    for _, row in abnormal.iterrows():
        test_name = str(row["Test Name"]).strip().replace(" ", "_").title()
        weight = RISK_WEIGHTS.get(test_name, DEFAULT_WEIGHT)
        score += weight
        flagged_tests.append(test_name)

    abnormal_count = len(abnormal)
    total_count    = len(df)
    abnormal_pct   = (abnormal_count / total_count) * 100 if total_count > 0 else 0

    # Determine level
    if score >= 15 or abnormal_pct >= 40:
        level = "High"
        message = (
            f"{abnormal_count} out of {total_count} values are abnormal "
            f"({abnormal_pct:.0f}%). Some results may need prompt medical attention. "
            "Please consult a doctor soon."
        )
    elif score >= 6 or abnormal_pct >= 20:
        level = "Moderate"
        message = (
            f"{abnormal_count} out of {total_count} values are outside the normal range. "
            "It is advisable to discuss these results with your doctor at your next visit."
        )
    else:
        level = "Low"
        message = (
            f"{abnormal_count} out of {total_count} values are slightly outside the normal range, "
            "but the overall picture looks manageable. Monitor and follow up with your doctor."
        )

    return level, message
