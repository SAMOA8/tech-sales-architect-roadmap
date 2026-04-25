# Day 12 — Zero Trust Architecture & Cloud Security Posture

## Zero Trust
**Principle:** "Never trust, always verify."

### Pillars
- **Identity** — verify who (MFA, federation)
- **Device** — verify trusted/compliant device
- **Network** — micro-segmentation, encrypt all traffic
- **Application** — auth at app layer, not just network
- **Data** — classify and protect regardless of location

### AWS Zero Trust Implementation
- IAM Identity Center (centralized identity)
- **AWS Verified Access** — Zero Trust app access without VPN
- AWS Network Firewall (deep packet inspection)
- **PrivateLink** (private service connectivity)
- Mutual TLS (mTLS)

## Cloud Security Posture Management (CSPM)
- Continuously monitors for misconfigurations
- AWS native: Security Hub + Config
- 3rd party: Prisma Cloud, Wiz, Lacework, Orca Security
- **Your audit tool is a basic CSPM!**

## Compliance Frameworks
| Framework | What | Key AWS Services |
|-----------|------|------------------|
| GDPR | EU data protection | Macie, KMS, Region selection |
| HIPAA | US healthcare | Artifact (BAA), KMS, CloudTrail, VPC |
| PCI DSS | Cardholder data | WAF, Shield, Security Hub, Config |
| SOC 2 | Security/availability/confidentiality | Artifact, IAM, Config |
| ISO 27001 | InfoSec management | Artifact |
| NIST 800-53 | US fed controls | Security Hub, Config |
| FedRAMP | US fed cloud auth | GovCloud, Artifact |

---

## Practice (30 min)
- [ ] "How would you position AWS to a CISO preparing for PCI DSS audit?"

---

## Self-Quiz
1. Zero Trust vs traditional perimeter security?
2. What is AWS Verified Access?
3. What is CSPM and which AWS services provide it?
4. Which AWS service is critical for HIPAA?
5. Why does GDPR require careful Region selection?
