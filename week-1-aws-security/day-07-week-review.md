# Day 7 — Week 1 Review & Mock Customer Scenario

## Self-Test (1 hour)
Answer aloud without notes:
1. What does the Shared Responsibility Model mean for a healthcare company?
2. How does KMS envelope encryption work?
3. Difference between WAF and Shield?
4. How does GuardDuty detect threats without agents?
5. CloudTrail vs CloudWatch?
6. When to recommend Shield Advanced over Standard?
7. SCP vs IAM policy?
8. Why does Macie matter for GDPR?
9. What does AWS Config do that CloudTrail doesn't?
10. Cognito vs IAM?

---

## Mock Sales Scenario (1 hour)

**Customer:** "We're moving our healthcare app to AWS. We store patient records and we're worried about compliance and security. What do you recommend?"

### Practice answering this aloud, covering:
- Shared Responsibility Model (data is your responsibility)
- **Encryption** — KMS for keys, S3 SSE-KMS for patient data at rest
- **Network** — VPC with private subnets, no public exposure
- **Access** — IAM least privilege, MFA all users, no root keys
- **Monitoring** — CloudTrail audit trail, GuardDuty for threats
- **Compliance** — Artifact for HIPAA BAA, Config for continuous compliance
- **Data discovery** — Macie to find any misplaced PII
- **Governance** — Organizations + SCPs to enforce security across accounts

---

## Update Hands-On Project (30 min)
- [ ] Re-run `python audit.py` against your AWS account
- [ ] Note improvements from any fixes you made
- [ ] Commit changes to GitHub

---

## Self-Assessment
Score yourself 1–10 on each:
- AWS Security service knowledge: ___/10
- Comfort explaining concepts to a non-technical person: ___/10
- Ability to map services to customer pain points: ___/10

**If any score is below 7 — revisit that day before moving to Week 2.**
