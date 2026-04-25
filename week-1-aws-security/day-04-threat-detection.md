# Day 4 — Threat Detection: GuardDuty, Inspector, Security Hub, Detective

## Amazon GuardDuty (1 hour)
- ML-based continuous threat detection
- **Data sources:** VPC Flow Logs, CloudTrail, DNS logs (+ optional S3, EKS, RDS, Lambda)
- **Detects:** crypto-mining, credential theft, port scanning, malicious IPs, unusual IAM behavior
- Findings flow into Security Hub automatically
- Severity: LOW / MEDIUM / HIGH / CRITICAL
- No agents required

## Amazon Inspector
- Automated vulnerability assessment
- Scans: EC2, ECR container images, Lambda functions
- Identifies CVEs, network reachability, prioritizes by risk score
- Integrates with Systems Manager for patching

## AWS Security Hub
- Central dashboard aggregating findings from: GuardDuty, Inspector, Macie, Firewall Manager, IAM Access Analyzer + 3rd party
- Compliance standards: CIS Benchmarks, FSBP, PCI DSS, NIST 800-53
- Security score and trend tracking

## Amazon Detective
- Visualizes and investigates security incidents
- ML behavior baselines
- Reduces Mean Time To Investigate (MTTI) — key SOC metric

---

## Practice (30 min)
- [ ] Enable GuardDuty in your AWS account (30-day free trial)
- [ ] Explore the GuardDuty console
- [ ] Write: "How would you explain GuardDuty to a CFO in 3 sentences?"

---

## Sales Talking Points
> "GuardDuty caught a customer's crypto-miner within 2 hours — saved them $50K in EC2 bills."
> "Security Hub gives your CISO one dashboard instead of logging into 10 different tools."

---

## Self-Quiz
1. What 3 default data sources does GuardDuty analyze?
2. How is Inspector different from GuardDuty?
3. What does Security Hub aggregate?
4. When would you recommend Amazon Detective?
5. What compliance frameworks does Security Hub support?
