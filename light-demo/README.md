# ReimBand Lightweight Streamlit Demo

ReimBand is a multi-agent reimbursement review workflow built for the Band of Agents Hackathon. It helps turn messy reimbursement materials into structured records, risk flags, and an explainable review trail.

## Why multi-agent reimbursement review?

Reimbursement review is not just OCR. A useful workflow needs several distinct roles:

- A document intake role that extracts invoice and payment facts.
- A policy role that checks whether required information is present.
- An audit role that reviews consistency, risk, and whether the case should be approved or rechecked.

Band is useful because it makes these roles visible as collaborating agents rather than hiding the whole process inside one chatbot response.

## What this lightweight demo shows

This Streamlit demo demonstrates the core ReimBand story without requiring private files, local backend services, OCR credits, Band API keys, or Qwen API keys.

The demo scenario uses the redacted/synthetic file name:

`demo_case_02_mar30_mar31_total_1990_20_minimal_redacted.pdf`

The file name indicates a reimbursement total of **1,990.20 CNY**. The cached review shows that OCR/review results include USD invoice records, that payment proof is missing or insufficient, and that cross-currency review is required. The multi-agent review recommends human review or recheck instead of blind approval.

## Relationship to the full ReimBand workflow

The full local ReimBand project includes:

- A local reimbursement review web app.
- OCR and parsing for invoices, bank statements, and payment screenshots.
- CSV export and printable reimbursement package generation.
- Band Remote Agents for Document Intake, Policy Specialist, and Audit Reviewer handoffs.

This lightweight demo is a deployable online preview for hackathon judges. It uses cached redacted data by default so the workflow can be reviewed safely on Streamlit Community Cloud.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Then open the local Streamlit URL shown in your terminal.

## Deploy on Streamlit Community Cloud

1. Push this folder to a public or private GitHub repository.
2. Go to Streamlit Community Cloud.
3. Create a new app from the repository.
4. Set the main file path to:

```text
streamlit_app.py
```

5. Deploy. No secrets are required for the default demo.

## Security and privacy

This demo intentionally uses cached redacted/synthetic data only.

It does not include:

- Real API keys.
- Band Agent API keys.
- Qwen or DashScope API keys.
- Real invoices.
- Personal financial documents.
- Required user secrets.

The `.streamlit/secrets.toml.example` file is included only as a placeholder for future live integrations.
