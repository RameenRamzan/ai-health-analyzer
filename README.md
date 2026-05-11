# 🩺 AI Health Report & Medicine Analyzer

A Streamlit web app that reads lab report PDFs, explains results in plain language using Gemini AI, and checks medicine interactions.

---

## Features

- **PDF Lab Report Upload** — Extracts test values from table-based PDFs automatically
- **Color-coded Results** — Each value is tagged Normal 🟢 / High 🔴 / Low 🟡
- **Risk Assessment** — Overall risk score based on which values are abnormal
- **AI Explanation** — Gemini AI explains what abnormal results mean in simple language
- **Follow-up Chat** — Ask any question about your results
- **Medicine Checker** — Checks for interactions using OpenFDA + Gemini AI

---

## Project Structure

```
Health_Analyzer/
├── app.py                        # Main Streamlit app
├── requirements.txt              # Dependencies
├── .env                          # API key (local only — do NOT commit)
├── assets/
│   └── disclaimer.md
├── data/
│   ├── reference_range.py        # Normal ranges for 50+ tests
│   └── aliases.py                # Alternative test name mappings
└── modules/
    ├── pdf_parser.py             # PDF extraction and parsing
    ├── classifier.py             # Value classification logic
    ├── gemini_client.py          # Gemini AI integration
    ├── medicine_checker.py       # OpenFDA + Gemini drug interaction checker
    └── risk_engine.py            # Risk scoring engine
```

---

## Local Setup

### 1. Clone or unzip the project

```bash
cd Health_Analyzer
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your Gemini API key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_key_here
```

Get a free key at: https://ai.google.dev

### 5. Run the app

```bash
streamlit run app.py
```

## Contributors

Rameen Ramzan [github.com](https://github.com/RameenRamzan)
Umama Zubair [github.com](https://github.com/uz352006/Umama-Zubair)

---

## Medical Disclaimer

This tool is for **informational purposes only** and does not constitute medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional regarding your lab results or medications.
