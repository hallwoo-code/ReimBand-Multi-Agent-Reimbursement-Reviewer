import json
from pathlib import Path

import pandas as pd
import streamlit as st

APP_DIR = Path(__file__).parent
DEMO_FILE_NAME = "demo_case_02_mar30_mar31_total_1990_20_minimal_redacted.pdf"
RECORDS_PATH = APP_DIR / "demo_data" / "demo_records.csv"
REVIEW_PATH = APP_DIR / "demo_data" / "demo_agent_review.json"

st.set_page_config(
    page_title="ReimBand | Multi-Agent Reimbursement Review",
    page_icon="RB",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --rb-bg: #f7f9fc;
        --rb-panel: #ffffff;
        --rb-text: #0f172a;
        --rb-muted: #64748b;
        --rb-line: #dbe4f0;
        --rb-blue: #2563eb;
        --rb-cyan: #06b6d4;
        --rb-green: #16a34a;
        --rb-amber: #d97706;
        --rb-red: #dc2626;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1180px;
    }
    .rb-hero {
        border: 1px solid var(--rb-line);
        border-radius: 18px;
        padding: 28px 30px;
        background: linear-gradient(135deg, #06142f 0%, #0b2b52 58%, #073042 100%);
        color: white;
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.16);
    }
    .rb-hero h1 {
        font-size: 3.2rem;
        line-height: 1;
        margin: 0 0 0.35rem 0;
        letter-spacing: 0;
    }
    .rb-hero p {
        color: #cbd5e1;
        font-size: 1.08rem;
        max-width: 820px;
        margin: 0.35rem 0 0 0;
    }
    .rb-pill {
        display: inline-block;
        border: 1px solid rgba(6, 182, 212, 0.55);
        background: rgba(6, 182, 212, 0.12);
        color: #a5f3fc;
        border-radius: 999px;
        padding: 6px 12px;
        margin: 0 8px 12px 0;
        font-size: 0.82rem;
        font-weight: 650;
    }
    .rb-card {
        border: 1px solid var(--rb-line);
        background: var(--rb-panel);
        border-radius: 14px;
        padding: 18px 18px;
        min-height: 128px;
        box-shadow: 0 10px 28px rgba(15, 23, 42, 0.06);
    }
    .rb-card h3 {
        margin: 0 0 8px 0;
        font-size: 1.02rem;
        color: var(--rb-text);
    }
    .rb-card p {
        color: var(--rb-muted);
        margin: 0;
        font-size: 0.95rem;
        line-height: 1.48;
    }
    .rb-agent-step {
        border-left: 4px solid var(--rb-blue);
        border-radius: 12px;
        padding: 16px 18px;
        background: #ffffff;
        border-top: 1px solid var(--rb-line);
        border-right: 1px solid var(--rb-line);
        border-bottom: 1px solid var(--rb-line);
        margin-bottom: 12px;
    }
    .rb-agent-step h4 {
        margin: 0 0 6px 0;
        color: var(--rb-text);
    }
    .rb-agent-step p {
        margin: 0;
        color: var(--rb-muted);
    }
    .rb-risk {
        padding: 10px 12px;
        border-radius: 10px;
        background: #fff7ed;
        border: 1px solid #fed7aa;
        color: #9a3412;
        margin-bottom: 8px;
        font-size: 0.94rem;
    }
    .rb-ok {
        padding: 10px 12px;
        border-radius: 10px;
        background: #ecfdf5;
        border: 1px solid #bbf7d0;
        color: #166534;
        margin-bottom: 8px;
        font-size: 0.94rem;
    }
    div[data-testid="stMetricValue"] {
        font-weight: 760;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_records() -> pd.DataFrame:
    df = pd.read_csv(RECORDS_PATH)
    return df


def load_review() -> dict:
    with REVIEW_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def money(value: float, currency: str = "CNY") -> str:
    return f"{value:,.2f} {currency}"


records = load_records()
review = load_review()

st.markdown(
    """
    <div class="rb-hero">
      <span class="rb-pill">Band of Agents Hackathon</span>
      <span class="rb-pill">Finance Workflow</span>
      <span class="rb-pill">Cached Online Demo</span>
      <h1>ReimBand</h1>
      <h2 style="margin:0;color:#e2e8f0;font-weight:520;">Multi-Agent Reimbursement Review</h2>
      <p>
        ReimBand turns messy reimbursement evidence into structured records and a traceable
        multi-agent review. This lightweight online demo uses redacted cached data so judges can
        experience the workflow without local services, private files, or API keys.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

left, right = st.columns([1.05, 1])
with left:
    st.subheader("Upload Evidence")
    uploaded_file = st.file_uploader(
        "Upload reimbursement evidence",
        type=["pdf", "png", "jpg", "jpeg"],
        help="The deployed demo reads cached redacted review data. The full local app can process real PDFs and images.",
    )
    if uploaded_file is None:
        st.info(
            f"Demo scenario: `{DEMO_FILE_NAME}`. Upload any PDF/image or click the button below to run the cached review."
        )
    else:
        st.success(f"Received `{uploaded_file.name}`. The online demo will use cached redacted review data.")

    run_review = st.button("Run OCR / Demo Review", type="primary", use_container_width=True)
    st.caption(
        "Online demo note: live OCR and Band API calls are disabled here. Cached redacted demo data is used when live OCR is unavailable."
    )

with right:
    st.subheader("What this demo proves")
    st.markdown(
        """
        <div class="rb-card">
          <h3>Core workflow</h3>
          <p>
          A reimbursement file is treated as evidence, converted into structured records,
          checked for payment proof and currency issues, then handed across three agent roles.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if not run_review:
    st.write("")
    st.warning("Click **Run OCR / Demo Review** to view the cached ReimBand review result.")
    st.stop()

st.divider()
st.header("Review Results")

summary = review["summary"]
metric_cols = st.columns(4)
metric_cols[0].metric("Record count", summary["record_count"])
metric_cols[1].metric("File-indicated total", money(summary["file_indicated_total_cny"], "CNY"))
metric_cols[2].metric("Detected invoice total", money(summary["detected_invoice_total_usd"], "USD"))
metric_cols[3].metric("Review status", summary["status"])

st.subheader("Risk Flags")
for flag in review["risk_flags"]:
    st.markdown(f"<div class='rb-risk'><strong>{flag['code']}</strong>: {flag['message']}</div>", unsafe_allow_html=True)

st.subheader("Quick Review")
quick_cols = st.columns(4)
quick_items = review["quick_review"]
for col, item in zip(quick_cols, quick_items):
    tone = "rb-ok" if item["status"] == "detected" else "rb-risk"
    col.markdown(
        f"<div class='{tone}'><strong>{item['label']}</strong><br>{item['detail']}</div>",
        unsafe_allow_html=True,
    )

st.subheader("Extracted Reimbursement Records")
st.dataframe(records, use_container_width=True, hide_index=True)

csv_bytes = records.to_csv(index=False).encode("utf-8-sig")
st.download_button(
    "Download CSV",
    data=csv_bytes,
    file_name="reimband_demo_records.csv",
    mime="text/csv",
    use_container_width=True,
)

st.divider()
st.header("Multi-Agent Review")
for idx, step in enumerate(review["agent_review"], start=1):
    st.markdown(
        f"""
        <div class="rb-agent-step">
          <h4>{idx}. {step['agent']}</h4>
          <p>{step['message']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.subheader("Band-style handoff summary")
st.markdown(
    """
    <div class="rb-card">
      <h3>Recommended outcome</h3>
      <p>
      The case should not be blindly approved. The file name indicates 1,990.20 CNY,
      while the extracted records include USD invoice lines and insufficient payment proof.
      ReimBand recommends human review or one recheck before approval.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()
st.header("Print Pack")
st.write(
    "The full local ReimBand version can generate printable reimbursement materials: original evidence pages, structured CSV records, and a review summary suitable for finance staff. This online demo focuses on the deployable multi-agent review story."
)
