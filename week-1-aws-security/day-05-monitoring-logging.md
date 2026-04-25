# Day 5 — Monitoring, Logging & Compliance

## AWS CloudTrail (1 hour)
- Records every API call: who, what, when, from where
- **Management events** (default, free) vs **Data events** (optional, charged)
- **CloudTrail Insights** — detects unusual API patterns
- Log file validation (SHA-256) for tamper detection
- Store in S3 with Object Lock for immutability

## Amazon CloudWatch
- Metrics, alarms, logs, dashboards
- **EventBridge** — serverless event bus, route AWS events to Lambda/SNS/SQS
- Custom metrics via CloudWatch Agent
- Default 1-min metric resolution; 1-sec for high-resolution

## AWS Config (1 hour)
- Continuously records resource configurations
- **Config Rules** — evaluate resources (COMPLIANT / NON_COMPLIANT)
- 150+ managed rules (e.g., s3-bucket-public-read-prohibited)
- **Conformance Packs** — bundled rules (PCI DSS, CIS, HIPAA)
- Auto-remediation via SSM Automation

## AWS Artifact
- Self-service compliance reports portal
- Reports: SOC 1/2/3, PCI DSS, ISO 27001, HIPAA BAA, FedRAMP
- Critical for regulated industries

## AWS Trusted Advisor
- 5 pillars: Cost, Performance, Security, Fault Tolerance, Service Limits
- Free security checks: open S3, MFA on root, exposed access keys, open ports

---

## Practice (30 min)
- [ ] Browse CloudTrail Event History — find a specific API call
- [ ] Practice: "A customer needs to prove HIPAA compliance. How does AWS help?"

---

## Sales Talking Points
> "CloudTrail is your black-box recorder for AWS — when something goes wrong, it tells you exactly who did what."
> "AWS Artifact means your compliance team downloads SOC 2 reports on demand instead of waiting months."

---

## Self-Quiz
1. CloudTrail vs CloudWatch — what does each capture?
2. Difference between Management and Data events?
3. What does AWS Config do that CloudTrail does not?
4. What is a Conformance Pack?
5. Which Trusted Advisor checks are free?
