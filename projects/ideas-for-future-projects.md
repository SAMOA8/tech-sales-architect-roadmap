# Future Project Ideas

## 1. AWS Compliance Checker (CIS AWS Foundations Benchmark)
A Python tool that evaluates an AWS account against all 50+ CIS AWS Foundations Benchmark v3.0 controls and generates a compliance report.

**Why it's valuable:** CIS Benchmarks are an industry-standard security framework. Demonstrating ability to automate compliance checking is directly applicable to the Tech Sales Architect role.

**Stack:** Python, boto3, Jinja2 for HTML reports

---

## 2. GuardDuty Findings → Slack Notifier
A serverless solution (Lambda + EventBridge) that listens to GuardDuty findings in real time and posts formatted alerts to a Slack channel based on severity.

**Why it's valuable:** Demonstrates serverless skills, security automation, and SOAR (Security Orchestration, Automation and Response) thinking — a hot topic in security sales.

**Stack:** AWS Lambda (Python), EventBridge, SNS, Slack webhook

---

## 3. Bedrock Guardrails Demo App
A small web app that lets users send prompts to Bedrock with and without Guardrails enabled, showing the security difference. Includes a curated set of prompt injection attempts.

**Why it's valuable:** Most companies want to adopt AI but are blocked by security concerns. A live demo of Guardrails in action is a powerful sales asset.

**Stack:** Python (Flask or FastAPI), Bedrock API, simple HTML/JS frontend

---

## 4. Multi-Cloud Security Comparison Dashboard
A document/dashboard that compares equivalent security services across AWS, Azure, and GCP — searchable and filterable by use case.

**Why it's valuable:** Multi-cloud awareness is a top requested skill for Sales Architects in 2026.

**Stack:** Markdown + GitHub Pages, or simple React app

---

## 5. AWS Security Cost Calculator
A spreadsheet/tool estimating monthly cost of common AWS security services (GuardDuty, Security Hub, Config, Macie) based on user inputs (number of accounts, data volume, region count).

**Why it's valuable:** ROI conversations are core Sales Architect skill. A pre-built calculator makes me more credible in customer meetings.

**Stack:** Excel or simple Python CLI
