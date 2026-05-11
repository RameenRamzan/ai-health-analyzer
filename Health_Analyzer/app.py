import streamlit as st
import pandas as pd

from modules.pdf_parser import parse_lab_report
from modules.classifier import build_results_table
from modules.medical_insights import generate_insight
from modules.gemini_client import explain_lab_results, answer_followup
from modules.medicine_checker import check_medicine_interactions
from modules.risk_engine import calculate_risk


st.set_page_config(
    page_title="🧠 AI Health Report & Medicine Analyzer",
    page_icon="🩺",
    layout="wide"
)

st.warning(
    "⚠ This tool is for informational purposes only. "
    "It does NOT provide medical diagnosis. "
    "Always consult a qualified doctor."
)

st.markdown("""
<style>
/* ── Card base ── */
.result-card {
    padding: 14px 18px;
    border-radius: 12px;
    margin-bottom: 12px;
    border-left: 6px solid #ccc;
    color: inherit;
}

/* ── Status variants — vivid enough for both light & dark modes ── */
.card-normal  { background: rgba(34, 197, 94,  0.18); border-left-color: #22c55e; }
.card-high    { background: rgba(239, 68,  68,  0.18); border-left-color: #ef4444; }
.card-low     { background: rgba(245, 158, 11,  0.18); border-left-color: #f59e0b; }
.card-unknown { background: rgba(156, 163, 175, 0.18); border-left-color: #9ca3af; }

/* ── Risk banners ── */
.risk-banner {
    padding: 14px 18px;
    border-radius: 10px;
    margin-bottom: 10px;
    font-size: 1rem;
    color: inherit;
}
.risk-low      { background: rgba(34, 197, 94,  0.20); border-left: 6px solid #22c55e; }
.risk-moderate { background: rgba(245, 158, 11,  0.20); border-left: 6px solid #f59e0b; }
.risk-high     { background: rgba(239, 68,  68,  0.20); border-left: 6px solid #ef4444; }

/* ── Status badge text colours — readable on both themes ── */
.status-normal  { color: #16a34a; font-weight: 700; }
.status-high    { color: #dc2626; font-weight: 700; }
.status-low     { color: #d97706; font-weight: 700; }
.status-unknown { color: #6b7280; font-weight: 700; }

/* ── Dark mode overrides for stronger contrast ── */
@media (prefers-color-scheme: dark) {
    .status-normal  { color: #4ade80; }
    .status-high    { color: #f87171; }
    .status-low     { color: #fbbf24; }
    .status-unknown { color: #9ca3af; }
}
</style>
""", unsafe_allow_html=True)

def get_ui_style(status: str):
    s = str(status).strip().lower()
    if s == "normal":
        return "card-normal", "🟢", "Normal", "status-normal"
    elif s == "high":
        return "card-high",   "🔴", "High",   "status-high"
    elif s == "low":
        return "card-low",    "🟡", "Low",    "status-low"
    else:
        return "card-unknown","⚪", "Unknown","status-unknown"

if "results_df" not in st.session_state:
    st.session_state.results_df = None
if "ai_data" not in st.session_state:
    st.session_state.ai_data = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🩺 AI Health Dashboard")

tab1, tab2 = st.tabs(["🧪 Lab Report Analysis", "💊 Medicine Checker"])

with tab1:

    col1, col2 = st.columns([3, 1])
    with col1:
        uploaded_file = st.file_uploader("Upload Lab Report (PDF)", type=["pdf"])
    with col2:
        gender = st.selectbox("Gender", ["general", "male", "female"])

    if uploaded_file:

        with st.spinner("Processing report..."):
            uploaded_file.seek(0)
            parsed = parse_lab_report(uploaded_file)

        if not parsed:
            st.error("❌ No data could be extracted from this PDF. "
                     "Make sure it contains a text-based (non-scanned) lab table.")
        else:
            df = build_results_table(parsed, gender)
            st.session_state.results_df = df

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Total Tests", len(df))
            c2.metric("🟢 Normal",   len(df[df["Status"] == "Normal"]))
            c3.metric("🔴 High",     len(df[df["Status"] == "High"]))
            c4.metric("🟡 Low",      len(df[df["Status"] == "Low"]))

            st.subheader("🧠 Risk Level")
            risk_level, risk_msg = calculate_risk(df)
            st.markdown(
                f"<div class='risk-banner risk-{risk_level.lower()}'>"
                f"<b>{risk_level} Risk</b><br>{risk_msg}"
                f"</div>",
                unsafe_allow_html=True
            )

            st.subheader("📋 Results")
            cols = st.columns(2)
            for i, (_, row) in enumerate(df.iterrows()):
                card_cls, icon, clean_status, status_cls = get_ui_style(row["Status"])
                with cols[i % 2]:
                    st.markdown(
                        f"""<div class="result-card {card_cls}">
                            <b>{row['Test Name']}</b> {icon}<br>
                            <b>{row['Value']} {row['Unit']}</b><br>
                            Status: <span class="{status_cls}">{clean_status}</span>
                        </div>""",
                        unsafe_allow_html=True
                    )

            st.divider()
            st.subheader("🤖 AI Explanation")

            if st.button("Generate AI Report"):
                with st.spinner("Asking AI..."):
                    ai_text = explain_lab_results(df)
                    st.session_state.ai_data = ai_text   # store raw text now

            if st.session_state.ai_data:
                st.markdown(st.session_state.ai_data)

            st.divider()
            st.subheader("💬 Ask Questions")

            for msg in st.session_state.chat_history:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])

            question = st.chat_input("Ask about your report...")
            if question:
                st.session_state.chat_history.append({"role": "user", "content": question})
                with st.chat_message("user"):
                    st.write(question)

                with st.spinner("Thinking..."):
                    answer = answer_followup(
                        question, df,
                        st.session_state.chat_history[:-1]   # history before this question
                    )

                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                with st.chat_message("assistant"):
                    st.write(answer)

with tab2:

    st.subheader("💊 Medicine Interaction Checker")

    meds = st.text_area(
        "Enter medicines (one per line)",
        placeholder="e.g.\nAspirin\nWarfarin\nMetformin"
    )

    if st.button("Check Interactions"):
        meds_list = [m.strip() for m in meds.split("\n") if m.strip()]

        if len(meds_list) < 2:
            st.warning("Please enter at least 2 medicines.")
        else:
            with st.spinner("Analysing interactions..."):
                result = check_medicine_interactions(meds_list)
            st.success("Analysis complete")
            st.markdown(result)

    st.caption("⚠ Always consult a licensed doctor before changing any medication.")