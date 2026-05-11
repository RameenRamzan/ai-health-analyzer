import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

MODEL = "gemini-2.5-flash"


def check_medicine_interactions(meds_list):

    if not meds_list or len(meds_list) < 2:
        return "Please enter at least two medicines."

    meds_text = "\n".join(meds_list)

    prompt = f"""
You are a medical safety assistant.

Check for possible interactions between these medicines:

{meds_text}

Return:
- Interaction risk level (Low / Moderate / High)
- Short explanation
- Precaution advice

Rules:
- Use simple language
- No diagnosis
- Be cautious and safe

Also include:
"This is not a medical diagnosis."

Answer:
"""

    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("Medicine AI Error:", e)
        return "Service unavailable. Please try again later."