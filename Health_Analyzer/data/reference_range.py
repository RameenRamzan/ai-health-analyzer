REFERENCE_RANGES = {

    "WBC": {
        "full_name": "White Blood Cell Count",
        "general": {"min": 4.5, "max": 11.0, "unit": "10³/µL"}
    },
    "RBC": {
        "full_name": "Red Blood Cell Count",
        "male":    {"min": 4.5, "max": 5.9, "unit": "10⁶/µL"},
        "female":  {"min": 4.1, "max": 5.1, "unit": "10⁶/µL"},
        "general": {"min": 4.1, "max": 5.9, "unit": "10⁶/µL"}
    },
    "Hemoglobin": {
        "full_name": "Hemoglobin",
        "male":    {"min": 13.5, "max": 17.5, "unit": "g/dL"},
        "female":  {"min": 12.0, "max": 15.5, "unit": "g/dL"},
        "general": {"min": 12.0, "max": 17.5, "unit": "g/dL"}
    },
    "Hematocrit": {
        "full_name": "Hematocrit",
        "male":    {"min": 38.3, "max": 48.6, "unit": "%"},
        "female":  {"min": 35.5, "max": 44.9, "unit": "%"},
        "general": {"min": 35.5, "max": 48.6, "unit": "%"}
    },
    "MCV": {
        "full_name": "Mean Corpuscular Volume",
        "general": {"min": 80, "max": 100, "unit": "fL"}
    },
    "MCH": {
        "full_name": "Mean Corpuscular Hemoglobin",
        "general": {"min": 27, "max": 33, "unit": "pg"}
    },
    "MCHC": {
        "full_name": "Mean Corpuscular Hemoglobin Concentration",
        "general": {"min": 32, "max": 36, "unit": "g/dL"}
    },
    "Platelets": {
        "full_name": "Platelet Count",
        "general": {"min": 150, "max": 400, "unit": "10³/µL"}
    },
    "Neutrophils": {
        "full_name": "Neutrophils (differential)",
        "general": {"min": 40, "max": 70, "unit": "%"}
    },
    "Lymphocytes": {
        "full_name": "Lymphocytes (differential)",
        "general": {"min": 20, "max": 40, "unit": "%"}
    },
    "Monocytes": {
        "full_name": "Monocytes (differential)",
        "general": {"min": 2, "max": 8, "unit": "%"}
    },
    "Eosinophils": {
        "full_name": "Eosinophils (differential)",
        "general": {"min": 1, "max": 4, "unit": "%"}
    },
    "Basophils": {
        "full_name": "Basophils (differential)",
        "general": {"min": 0, "max": 1, "unit": "%"}
    },

    "Glucose_Fasting": {
        "full_name": "Glucose (Fasting)",
        "general": {"min": 70, "max": 100, "unit": "mg/dL"}
    },
    "Glucose_Random": {
        "full_name": "Glucose (Random)",
        "general": {"min": 70, "max": 140, "unit": "mg/dL"}
    },
    "HbA1c": {
        "full_name": "Glycated Hemoglobin",
        "general": {"min": 4.0, "max": 5.6, "unit": "%"}
    },
    "Insulin_Fasting": {
        "full_name": "Fasting Insulin",
        "general": {"min": 2.6, "max": 24.9, "unit": "µIU/mL"}
    },
    "C_Peptide": {
        "full_name": "C-Peptide",
        "general": {"min": 0.5, "max": 2.0, "unit": "ng/mL"}
    },

    "Total_Cholesterol": {
        "full_name": "Total Cholesterol",
        "general": {"min": 0, "max": 200, "unit": "mg/dL"}
    },
    "LDL": {
        "full_name": "LDL Cholesterol",
        "general": {"min": 0, "max": 100, "unit": "mg/dL"}
    },
    "HDL": {
        "full_name": "HDL Cholesterol",
        "male":    {"min": 40, "max": 999, "unit": "mg/dL"},
        "female":  {"min": 50, "max": 999, "unit": "mg/dL"},
        "general": {"min": 40, "max": 999, "unit": "mg/dL"}
    },
    "Triglycerides": {
        "full_name": "Triglycerides",
        "general": {"min": 0, "max": 150, "unit": "mg/dL"}
    },

    "ALT": {
        "full_name": "Alanine Aminotransferase",
        "male":    {"min": 7, "max": 56, "unit": "U/L"},
        "female":  {"min": 7, "max": 45, "unit": "U/L"},
        "general": {"min": 7, "max": 56, "unit": "U/L"}
    },
    "AST": {
        "full_name": "Aspartate Aminotransferase",
        "general": {"min": 10, "max": 40, "unit": "U/L"}
    },
    "ALP": {
        "full_name": "Alkaline Phosphatase",
        "general": {"min": 44, "max": 147, "unit": "U/L"}
    },
    "GGT": {
        "full_name": "Gamma-Glutamyl Transferase",
        "male":    {"min": 8, "max": 61, "unit": "U/L"},
        "female":  {"min": 5, "max": 36, "unit": "U/L"},
        "general": {"min": 5, "max": 61, "unit": "U/L"}
    },
    "Total_Bilirubin": {
        "full_name": "Total Bilirubin",
        "general": {"min": 0.1, "max": 1.2, "unit": "mg/dL"}
    },
    "Direct_Bilirubin": {
        "full_name": "Direct (Conjugated) Bilirubin",
        "general": {"min": 0.0, "max": 0.3, "unit": "mg/dL"}
    },
    "Total_Protein": {
        "full_name": "Total Protein",
        "general": {"min": 6.0, "max": 8.3, "unit": "g/dL"}
    },
    "Albumin": {
        "full_name": "Albumin",
        "general": {"min": 3.5, "max": 5.0, "unit": "g/dL"}
    },

    "Creatinine": {
        "full_name": "Creatinine",
        "male":    {"min": 0.74, "max": 1.35, "unit": "mg/dL"},
        "female":  {"min": 0.59, "max": 1.04, "unit": "mg/dL"},
        "general": {"min": 0.59, "max": 1.35, "unit": "mg/dL"}
    },
    "BUN": {
        "full_name": "Blood Urea Nitrogen",
        "general": {"min": 7, "max": 20, "unit": "mg/dL"}
    },
    "Uric_Acid": {
        "full_name": "Uric Acid",
        "male":    {"min": 3.4, "max": 7.0, "unit": "mg/dL"},
        "female":  {"min": 2.4, "max": 6.0, "unit": "mg/dL"},
        "general": {"min": 2.4, "max": 7.0, "unit": "mg/dL"}
    },
    "eGFR": {
        "full_name": "Estimated Glomerular Filtration Rate",
        "general": {"min": 60, "max": 999, "unit": "mL/min/1.73m²"}
    },

    "Sodium": {
        "full_name": "Sodium",
        "general": {"min": 136, "max": 145, "unit": "mEq/L"}
    },
    "Potassium": {
        "full_name": "Potassium",
        "general": {"min": 3.5, "max": 5.1, "unit": "mEq/L"}
    },
    "Chloride": {
        "full_name": "Chloride",
        "general": {"min": 98, "max": 107, "unit": "mEq/L"}
    },
    "Bicarbonate": {
        "full_name": "Bicarbonate (CO₂)",
        "general": {"min": 22, "max": 29, "unit": "mEq/L"}
    },
    "Calcium": {
        "full_name": "Total Calcium",
        "general": {"min": 8.5, "max": 10.5, "unit": "mg/dL"}
    },
    "Magnesium": {
        "full_name": "Magnesium",
        "general": {"min": 1.7, "max": 2.2, "unit": "mg/dL"}
    },
    "Phosphorus": {
        "full_name": "Phosphorus",
        "general": {"min": 2.5, "max": 4.5, "unit": "mg/dL"}
    },

    "TSH": {
        "full_name": "Thyroid-Stimulating Hormone",
        "general": {"min": 0.4, "max": 4.0, "unit": "mIU/L"}
    },
    "T3": {
        "full_name": "Total Triiodothyronine",
        "general": {"min": 80, "max": 200, "unit": "ng/dL"}
    },
    "T4": {
        "full_name": "Total Thyroxine",
        "general": {"min": 5.0, "max": 12.0, "unit": "µg/dL"}
    },
    "Free_T3": {
        "full_name": "Free Triiodothyronine",
        "general": {"min": 2.3, "max": 4.2, "unit": "pg/mL"}
    },
    "Free_T4": {
        "full_name": "Free Thyroxine",
        "general": {"min": 0.8, "max": 1.8, "unit": "ng/dL"}
    },

   "PT": {
        "full_name": "Prothrombin Time",
        "general": {"min": 11.0, "max": 13.5, "unit": "seconds"}
    },
    "INR": {
        "full_name": "International Normalized Ratio",
        "general": {"min": 0.8, "max": 1.1, "unit": "ratio"},
        "therapeutic": {"min": 2.0, "max": 3.0, "unit": "ratio"}
    },
    "aPTT": {
        "full_name": "Activated Partial Thromboplastin Time",
        "general": {"min": 25, "max": 35, "unit": "seconds"}
    },
    "Fibrinogen": {
        "full_name": "Fibrinogen",
        "general": {"min": 200, "max": 400, "unit": "mg/dL"}
    },

    "Troponin_I": {
        "full_name": "Troponin I (high-sensitivity)",
        "general": {"min": 0.0, "max": 0.04, "unit": "ng/mL"}
    },
    "CK_MB": {
        "full_name": "Creatine Kinase-MB",
        "general": {"min": 0.0, "max": 5.0, "unit": "ng/mL"}
    },
    "BNP": {
        "full_name": "B-type Natriuretic Peptide",
        "general": {"min": 0, "max": 100, "unit": "pg/mL"}
    },

    "Serum_Iron": {
        "full_name": "Serum Iron",
        "male":    {"min": 60,  "max": 170, "unit": "µg/dL"},
        "female":  {"min": 50,  "max": 170, "unit": "µg/dL"},
        "general": {"min": 50,  "max": 170, "unit": "µg/dL"}
    },
    "Ferritin": {
        "full_name": "Ferritin",
        "male":    {"min": 24,  "max": 336, "unit": "ng/mL"},
        "female":  {"min": 11,  "max": 307, "unit": "ng/mL"},
        "general": {"min": 11,  "max": 336, "unit": "ng/mL"}
    },
    "TIBC": {
        "full_name": "Total Iron-Binding Capacity",
        "general": {"min": 240, "max": 450, "unit": "µg/dL"}
    },
    "Transferrin_Sat": {
        "full_name": "Transferrin Saturation",
        "general": {"min": 20, "max": 50, "unit": "%"}
    },

    "Vitamin_D": {
        "full_name": "25-Hydroxyvitamin D",
        "general": {"min": 20, "max": 50, "unit": "ng/mL"}
    },
    "Vitamin_B12": {
        "full_name": "Vitamin B12 (Cobalamin)",
        "general": {"min": 200, "max": 900, "unit": "pg/mL"}
    },
    "Folate": {
        "full_name": "Folate (Serum)",
        "general": {"min": 2.7, "max": 17.0, "unit": "ng/mL"}
    },

    "CRP": {
        "full_name": "C-Reactive Protein",
        "general": {"min": 0.0, "max": 1.0, "unit": "mg/L"}
    },
    "ESR": {
        "full_name": "Erythrocyte Sedimentation Rate",
        "male":    {"min": 0, "max": 15, "unit": "mm/hr"},
        "female":  {"min": 0, "max": 20, "unit": "mm/hr"},
        "general": {"min": 0, "max": 20, "unit": "mm/hr"}
    },
}