import time
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")
genai.configure(api_key=api_key)

MODEL = "gemini-2.5-flash"


def safe_generate(prompt):
    for _ in range(3):
        try:
            model = genai.GenerativeModel(MODEL)
            res = model.generate_content(prompt)
            return res.text
        except Exception as e:
            print("Gemini Error:", e)
            time.sleep(2)

    return "Service busy. Try again later."


def format_results(df):
    if df is None or df.empty:
        return "No lab data available."

    lines = []
    for _, r in df.iterrows():
        try:
            lines.append(
                f"{r.get('Test Name', '')}: {r.get('Value', '')} {r.get('Unit', '')} ({r.get('Status', '')})"
            )
        except:
            continue

    return "\n".join(lines) if lines else "No valid lab data."


def explain_lab_results(df):

    data_text = format_results(df)

    prompt = f"""
You are a friendly medical assistant explaining lab results to a patient in simple everyday language.

Write a detailed but easy-to-understand explanation. Follow this structure:

1. Start with a brief 1-2 sentence overall summary of the report.
2. For each ABNORMAL test: explain what the test measures, what the abnormal value means, what it could indicate, and any general lifestyle or follow-up advice (2-3 sentences each).
3. For NORMAL tests: mention them together in one short paragraph saying they look healthy.
4. End with a short closing note reminding the patient to consult their doctor.

Rules:
- No tables, no JSON, no markdown headers, no cards
- Use plain paragraph style — flowing sentences, easy to read
- Use simple everyday words, avoid heavy medical jargon
- Be warm and reassuring in tone, not alarming
- Keep the total response between 200-300 words

DATA:
{data_text}
"""

    return safe_generate(prompt)


def answer_followup(question, df, history):

    history_text = ""
    for msg in history:
        history_text += f"{msg['role']}: {msg['content']}\n"

    data_text = format_results(df)

    prompt = f"""
You are a medical assistant.

Previous conversation:
{history_text}

DATA:
{data_text}

QUESTION:
{question}

Rules:
- Answer in simple language
- 3–5 lines only
- Do NOT give diagnosis

Answer:
"""

    return safe_generate(prompt)

def parse_to_cards(text):
    cards = []

    for line in text.split("\n"):
        parts = [p.strip() for p in line.split("|")]

        if len(parts) == 4:
            status_text = parts[3].lower()

            if "low" in status_text:
                clean_status = "Low"
            elif "high" in status_text:
                clean_status = "High"
            elif "normal" in status_text:
                clean_status = "Normal"
            else:
                clean_status = "Unknown"

            cards.append({
                "test": parts[0],
                "value": parts[1],
                "range": parts[2],
                "status": clean_status
            })

    return cards