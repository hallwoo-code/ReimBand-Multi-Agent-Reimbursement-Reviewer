# ReimBand: Multi-Agent Reimbursement Reviewer

ReimBand is a Band-powered multi-agent reimbursement review system designed for the **Band of Agents Hackathon**. It helps automate and coordinate reimbursement review by combining document extraction, policy checking, financial auditing, and human review coordination in one transparent multi-agent workflow.

Instead of relying on a single chatbot to make unsupported decisions, ReimBand uses a team of specialized agents that communicate through Band. Each agent has a clear responsibility, passes structured information to the next agent, and can request rechecks when information is missing, uncertain, or inconsistent.

---

## 🚀 Project Overview

Manual reimbursement review is often slow, fragmented, and error-prone. Reviewers need to check invoices, payment records, policy requirements, supporting documents, currency amounts, and possible risks across multiple files and systems.

ReimBand turns this workflow into a coordinated multi-agent process:

1. **Document Intake Agent** extracts structured information from invoices, receipts, payment records, and PDF documents.
2. **Policy Specialist Agent** checks reimbursement rules, required materials, and compliance evidence.
3. **Audit Reviewer Agent** compares extracted data with policy requirements, detects mismatches, flags risks, and decides whether the case can pass or requires human review.

The goal is not to fully replace human finance staff, but to reduce repetitive checking work, surface risks earlier, and make the review process more explainable and auditable.

---

## 🧠 Multi-Agent Architecture

ReimBand uses Band as the collaboration layer for agent communication, task handoff, and shared context.

```text
User / Reimbursement Case
        |
        v
Document Intake Agent
- Extracts invoice and payment information
- Normalizes structured fields
- Flags uncertain or missing data
        |
        v
Policy Specialist Agent
- Retrieves or applies reimbursement rules
- Checks required supporting documents
- Provides policy evidence
        |
        v
Audit Reviewer Agent
- Compares invoice and payment amounts
- Detects missing materials and risks
- Requests rechecks when necessary
- Produces the final review result
```

---

## 🤖 Agents

### 1. Document Intake Agent

The Document Intake Agent is responsible for reading reimbursement-related documents and extracting structured data.

It focuses on:

* Invoice amount
* Payment amount
* Currency
* Invoice number
* Expense type
* Provided documents
* Missing or uncertain fields
* OCR confidence when available

It does **not** make the final reimbursement decision. Instead, it passes the structured case to the Policy Specialist Agent.

---

### 2. Policy Specialist Agent

The Policy Specialist Agent checks whether the reimbursement case satisfies policy requirements.

It focuses on:

* Reimbursement category identification
* Required supporting materials
* Missing documents
* Policy evidence
* Ambiguous or unresolved policy questions

It sends the policy assessment and the original structured case to the Audit Reviewer Agent.

---

### 3. Audit Reviewer Agent

The Audit Reviewer Agent performs the final risk-oriented review.

It focuses on:

* Invoice and payment amount matching
* Missing required materials
* Uncertain critical fields
* Risk level assessment
* Human review recommendation
* Final review result

If key information is uncertain, the Audit Reviewer Agent can request a recheck from the Document Intake Agent.

---

## ✨ Key Features

* Multi-agent reimbursement review workflow
* Band-based agent communication and task handoff
* OCR-based invoice and document extraction
* Structured reimbursement case generation
* Policy requirement checking
* Amount mismatch detection
* Missing material detection
* Risk level classification
* Human review coordination
* Transparent and auditable agent messages

---

## 🛠️ Technologies Used

* **Band Agentic Mesh** — multi-agent communication and collaboration
* **Qwen / Qwen-VL OCR** — invoice and document understanding
* **Python** — agent logic and backend integration
* **Remote Agents** — locally running agents connected to Band
* **RAG / Policy Knowledge Base** — reimbursement rule retrieval and policy checking
* **OCR + Structured Extraction** — converting receipts and payment records into reviewable data

---

## 📌 Example Use Case

A user uploads or describes a reimbursement case:

```text
Expense type: conference registration fee
Invoice amount: 1990.20 USD
Payment amount: 1980.20 USD
Invoice number: INV-2026-0315
Provided documents:
- invoice
- payment record

Missing document:
- conference notice
```

The agents then coordinate:

1. **Document Intake Agent** extracts the structured case.
2. **Policy Specialist Agent** checks that conference registration reimbursement requires an invoice, payment record, and conference notice.
3. **Audit Reviewer Agent** detects that the payment amount does not match the invoice amount and that the conference notice is missing.
4. The final result is marked as high risk or requiring human review.

Example output:

```json
{
  "amount_match": false,
  "amount_difference": "10.00 USD",
  "missing_documents": ["conference notice"],
  "risk_level": "high",
  "decision": "HUMAN_REVIEW_REQUIRED",
  "reasons": [
    "Invoice amount and payment amount do not match.",
    "A required supporting document is missing."
  ]
}
```

---

## 🎯 Why Band?

Band is used as the coordination layer between specialized agents. In ReimBand, agents do not simply respond independently. They pass structured information, mention the next responsible agent, and create a visible audit trail of the review process.

Band enables:

* Multi-agent task handoff
* Shared conversation context
* Visible review chain
* Recheck loops
* Human-in-the-loop coordination
* Clear separation of agent responsibilities

This makes the reimbursement workflow more transparent than a single black-box chatbot.

---

## 🧪 Current Status

This project is currently a hackathon prototype.

Implemented or planned prototype components include:

* Remote Agent registration on Band
* Three-agent reimbursement review flow
* Qwen-powered document understanding
* Demo reimbursement cases
* Policy checking logic
* Risk review logic
* Human review recommendation

Future improvements may include:

* Full invoice image upload support
* Richer university and enterprise policy knowledge bases
* Excel / CSV / PDF export
* More reimbursement categories
* Persistent audit logs
* Web dashboard integration
* Enterprise finance system integration

---

## 📹 Demo

Demo video: `Coming soon`

Live demo: `Coming soon`

Slides: `Coming soon`

---

## 🔐 Security and Privacy

ReimBand is designed with privacy in mind. Sensitive credentials such as API keys are not stored in the repository.

The project should use local environment variables for:

* Band Agent API keys
* Qwen / model provider API keys
* OCR service credentials
* Any private reimbursement data paths

Real invoices, payment records, and private financial documents should not be committed to GitHub.

---

## 🧩 Project Structure

```text
ReimBand-Multi-Agent-Reimbursement-Reviewer/
├── README.md
├── band_agents/
│   ├── run_agent.py
│   ├── prompts/
│   │   ├── intake.md
│   │   ├── policy.md
│   │   └── audit.md
│   ├── tools/
│   │   ├── ocr_adapter.py
│   │   └── audit_tool.py
│   └── demo/
│       ├── demo_case.json
│       └── cached_ocr_result.json
├── assets/
│   └── cover.png
└── .env.example
```

---

## 🏆 Hackathon Track

Built for the **Band of Agents Hackathon**.

Relevant tracks and categories:

* Agent Builder Track - The INTERNET OF AGENTS
* Internal Enterprise Workflows
* Multi-Agent Software Development
* Business
* Finance
* Chatbot

---

## 📄 License

This project is for hackathon demonstration and educational purposes. License information will be updated later.
