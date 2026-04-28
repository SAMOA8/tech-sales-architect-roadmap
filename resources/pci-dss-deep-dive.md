# PCI DSS Deep Dive
## Payment Card Industry Data Security Standard

> Reference notes for Tech Sales Architect conversations with retail, e-commerce, fintech, and payment processing customers.

---

## What It Is

A global security standard for any organization that **stores, processes, or transmits cardholder data** — credit, debit, and prepaid cards. Created and maintained by the **PCI Security Standards Council (PCI SSC)**, founded by Visa, Mastercard, American Express, Discover, and JCB.

## Current Version
- **PCI DSS v4.0.1** (released June 2024)
- Full enforcement as of **March 31, 2025** — v3.2.1 retired
- Future-dated v4.0 requirements became mandatory March 2025

---

## Who Must Comply

Any business that handles cardholder data:
- E-commerce websites
- Retail stores
- Payment processors
- Service providers (cloud, hosting)
- SaaS that touches payment data

### Compliance Levels (by annual transaction volume)
| Level | Transactions/Year | Validation |
|-------|------------------|------------|
| 1 | 6M+ | External QSA audit |
| 2 | 1M–6M | SAQ + ASV scan |
| 3 | 20K–1M | SAQ + ASV scan |
| 4 | <20K | SAQ |

---

## The 12 Core Requirements (Grouped into 6 Goals)

### Goal 1 — Build & Maintain a Secure Network
1. **Install and maintain network security controls** (firewalls, segmentation)
2. **Apply secure configurations** to all system components (no default passwords)

### Goal 2 — Protect Cardholder Data
3. **Protect stored cardholder data** (encryption, masking, truncation, hashing)
4. **Protect cardholder data with strong cryptography during transmission**

### Goal 3 — Maintain a Vulnerability Management Program
5. **Protect all systems from malware** (anti-virus, EDR)
6. **Develop and maintain secure systems and software** (patching, secure coding)

### Goal 4 — Implement Strong Access Control
7. **Restrict access to cardholder data by business need-to-know**
8. **Identify users and authenticate access** (unique IDs, MFA)
9. **Restrict physical access to cardholder data**

### Goal 5 — Regularly Monitor and Test Networks
10. **Log and monitor all access** to network and cardholder data
11. **Test security of systems and networks regularly** (vuln scans, pen tests)

### Goal 6 — Maintain an Information Security Policy
12. **Support information security with organizational policies and programs**

---

## Key Concepts

### Cardholder Data (CHD) — must be protected
- **Primary Account Number (PAN)** — 16-digit card number
- Cardholder Name
- Expiration Date
- Service Code

### Sensitive Authentication Data (SAD) — must NEVER be stored after authorization
- Full magnetic stripe data
- CVV / CVC / CID (3-4 digit security code)
- PIN / PIN block

### CDE (Cardholder Data Environment)
The systems, people, and processes that store, process, or transmit CHD. PCI DSS scope = your CDE + anything connected to it.

### Tokenization
Replace PAN with a non-sensitive token; the original PAN is stored in a vault. Reduces PCI scope dramatically.

### P2PE (Point-to-Point Encryption)
Encrypts card data at the point of capture (terminal) until it reaches a secure decryption environment. Reduces scope.

---

## What's New in PCI DSS v4.0

- **Customized Approach** — meet objectives without prescriptive controls (mature orgs only)
- **MFA required for ALL access into the CDE** (not just admin)
- **Stronger password requirements** — 12 characters minimum
- **Authenticated internal vulnerability scans** (was unauthenticated)
- **Targeted risk analysis** for many control frequencies
- **Anti-phishing controls** required
- **Inventory of cryptographic cipher suites and protocols**
- **Enhanced requirements for service providers**
- **Annual scope confirmation** for service providers

---

## How AWS Helps with PCI DSS

| Requirement | AWS Service |
|-------------|-------------|
| Req 1 — Network security | VPC, Security Groups, NACLs, WAF, Shield, Network Firewall |
| Req 2 — Secure configs | AWS Config, Systems Manager, Trusted Advisor |
| Req 3 — Protect stored data | KMS, S3 SSE-KMS, RDS encryption, Macie |
| Req 4 — Encrypt transmission | ACM (TLS certs), TLS-only enforcement |
| Req 5 — Anti-malware | GuardDuty, Inspector, partner EDR (CrowdStrike) |
| Req 6 — Patching, secure SDLC | Inspector, CodeGuru Security, Systems Manager Patch Manager |
| Req 7 — Need-to-know access | IAM least privilege, permission boundaries, SCPs |
| Req 8 — Auth & MFA | IAM Identity Center, MFA enforcement |
| Req 9 — Physical security | AWS handles (data center) |
| Req 10 — Logging | CloudTrail, CloudWatch Logs, VPC Flow Logs, Security Hub |
| Req 11 — Testing | Inspector, GuardDuty, AWS-approved pen testing |
| Req 12 — Policy program | AWS Artifact (PCI DSS AOC), Audit Manager |

**AWS itself** is PCI DSS Level 1 Service Provider certified — customers can download AWS's PCI DSS Attestation of Compliance (AOC) from **AWS Artifact**.

### Built-In AWS Tools for PCI DSS
- **AWS Security Hub PCI DSS standard** — automated continuous compliance checks
- **AWS Config PCI DSS Conformance Pack** — deployable bundle of compliance rules
- **AWS Audit Manager PCI DSS framework** — automated evidence collection

---

## Sales Talking Points

> "AWS is PCI DSS Level 1 — the highest service provider tier. You inherit security from the certified infrastructure layer, but you still own the application and configuration layer. That's where Security Hub's PCI DSS standard, the Config conformance pack, and KMS encryption become essential."

> "PCI DSS v4.0 made MFA mandatory for ALL CDE access — not just admins. If your customers haven't deployed IAM Identity Center with MFA enforcement, they're already non-compliant as of March 2025."

> "Tokenization can shrink your PCI scope by 90%. Instead of treating your entire AWS environment as the CDE, isolate the token vault and let the rest of your infrastructure deal only with non-sensitive tokens."

> "An average PCI DSS audit takes 6 months. With Security Hub's PCI standard turned on, your auditor walks in and sees a real-time compliance dashboard — that often cuts audit time in half."

---

## Penalties for Non-Compliance

- Fines: **$5,000–$100,000 per month** until compliance achieved
- Card brands can revoke processing privileges
- Increased transaction fees
- Liability for fraud losses
- Mandatory forensic investigation after a breach
- Reputational damage and customer loss
- Class action lawsuits

---

## Discovery Questions for PCI DSS Customers

1. What is your current PCI DSS compliance level (1, 2, 3, 4)?
2. When is your next audit?
3. Have you achieved v4.0 compliance yet?
4. Do you have MFA on all access into the CDE?
5. Are you using tokenization or P2PE today?
6. How is your CDE segmented from the rest of your environment?
7. Who is your QSA?
8. Have you had any compliance findings in past audits?
9. How are you currently handling vulnerability scanning (ASV)?
10. Where is your cardholder data stored — on-premises, in AWS, both?

---

## Acronym Cheat Sheet

| Acronym | Meaning |
|---------|---------|
| QSA | Qualified Security Assessor (audits Level 1) |
| ISA | Internal Security Assessor |
| ASV | Approved Scanning Vendor (external vuln scans) |
| AOC | Attestation of Compliance |
| ROC | Report on Compliance |
| SAQ | Self-Assessment Questionnaire |
| CDE | Cardholder Data Environment |
| CHD | Cardholder Data |
| SAD | Sensitive Authentication Data |
| PAN | Primary Account Number |
| P2PE | Point-to-Point Encryption |

---

## Self-Quiz

1. Name the 12 PCI DSS core requirements grouped into 6 goals.
2. What's the difference between CHD and SAD? What can never be stored?
3. What changed for MFA in v4.0?
4. What is the CDE and why does its scope matter?
5. How does tokenization reduce PCI scope?
6. Where do you find AWS's PCI DSS AOC?
7. Which AWS service auto-checks PCI DSS compliance continuously?
8. What is a QSA vs ISA vs ASV?
9. What are the financial penalties for non-compliance?
10. What's new for service providers in v4.0?
