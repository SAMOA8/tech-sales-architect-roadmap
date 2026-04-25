# Day 16 — ROI, TCO & Business Case Building

## Formulas
- **ROI** = (Gain - Cost) / Cost × 100
- **TCO** = Total Cost of Ownership (cloud vs on-prem)

## Cost-of-Inaction Data Points
- IBM 2024 Report: avg breach cost = **$4.88M**
- Downtime: avg **$9,000/min** for large enterprises
- GDPR fines: up to **4% of global revenue**
- Security engineer cost: avg **$120K/year**

## Building a Security ROI Argument
- GuardDuty at $100/mo vs analyst at $10K/mo
- "GuardDuty caught crypto miner that would have been $50K in EC2 bills"
- Macie at $100/mo vs $20M GDPR fine
- Shield Advanced at $3K/mo vs $100K+ DDoS downtime

## AWS Pricing Models
- **On-Demand** — pay per second/hour
- **Reserved** — 1- or 3-year commitment, up to 72% savings
- **Savings Plans** — flexible commitment
- **Spot** — up to 90% off (interruptible)
- **Free Tier** — 12 months for new accounts

## Security Service Pricing Logic
- GuardDuty — per GB analyzed
- Security Hub — per check per month
- Macie — per GB of S3 scanned
- CloudTrail — first trail free
- Config — per configuration item recorded

---

## Practice (30 min)
- [ ] Customer pays $2K/mo for GuardDuty + Security Hub. Avoids 1 incident/yr at $500K. ROI?
- ROI = ($500K - $24K) / $24K × 100 = **1,983%**

---

## Self-Quiz
1. What is ROI vs TCO?
2. How do you justify a $36K/year GuardDuty bill?
3. Pricing model for Macie?
4. Reserved Instances vs Savings Plans?
5. How do compliance certifications affect revenue?
