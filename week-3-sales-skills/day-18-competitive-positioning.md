# Day 18 — Competitive Positioning

## AWS vs Azure vs GCP

### AWS Strengths
- Largest service catalog and ecosystem
- Most mature security services
- Most compliance certifications
- Native integration between security services

### AWS Weaknesses
- Complex pricing
- Steeper learning curve
- Weaker SIEM than Sentinel

### Azure Strengths
- Best Microsoft integration (AD, M365)
- Sentinel is best-in-class SIEM
- Strong hybrid (Azure Arc)

### Azure Weaknesses
- Smaller global infrastructure
- AI locked to OpenAI

### GCP Strengths
- Best AI/ML (Vertex AI, Gemini)
- BigQuery is best cloud data warehouse
- Strong Kubernetes (GKE)

### GCP Weaknesses
- Smallest enterprise footprint
- Fewer compliance certifications

## Third-Party Security Vendors
| Vendor | Category | Position |
|--------|----------|----------|
| CrowdStrike | EDR | Integrates with Security Hub |
| Palo Alto Prisma Cloud | CSPM/CWPP | Competes with Security Hub |
| Wiz | Agentless cloud security | Complements AWS native |
| Splunk | SIEM | Ingests CloudTrail/GuardDuty |
| Datadog | Monitoring | Competes with CloudWatch |
| HashiCorp Vault | Secrets | Competes with Secrets Manager |
| Okta | Identity | Complements IAM Identity Center |

---

## Practice
- [ ] "Customer says Wiz is already scanning AWS. Why need Security Hub too?"
- Answer: Security Hub centralizes findings (Wiz + GuardDuty + Inspector + Macie), AWS-native compliance frameworks, no extra cost for the aggregation
