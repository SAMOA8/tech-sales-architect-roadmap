# Day 2 — Data Security: KMS, Macie, S3 Security

## Encryption Fundamentals (1 hour)

- **Symmetric** — same key encrypts/decrypts (AES-256), fast, bulk data
- **Asymmetric** — public/private key pair (RSA), for key exchange and signatures
- **At rest:** S3 SSE, EBS encryption, RDS encryption
- **In transit:** TLS/SSL on all API calls, HTTPS endpoints

## AWS KMS (Key Management Service)

- 3 key types: AWS Owned, AWS Managed, Customer Managed (CMK)
- **Envelope encryption** — data key encrypts data, CMK encrypts the data key
- **Key rotation** — automatic annual rotation for CMKs
- Integrates with: S3, EBS, RDS, Lambda, Secrets Manager, Bedrock

## Amazon Macie (1 hour)
- Uses ML to discover sensitive data in S3
- Detects: PII (SSN, names, passport numbers), financial data, credentials, API keys
- Severity-rated findings → Security Hub
- Sales pitch: "Macie finds data you didn't know you had exposed"

## S3 Security Controls
- **Block Public Access** (4 settings: BlockPublicAcls, IgnorePublicAcls, BlockPublicPolicy, RestrictPublicBuckets)
- Bucket policies vs ACLs
- **S3 Object Lock** (WORM — compliance immutability)
- **S3 Versioning** (ransomware protection)
- **MFA Delete** (require MFA to permanently delete)
- SSE-S3 vs SSE-KMS vs SSE-C

---

## Practice (30 min)
- [ ] Check S3 Block Public Access account settings in console
- [ ] Write 2-min elevator pitch: "Why does your company need KMS?"

---

## Sales Talking Points
> "Macie found a customer's SSNs in an unencrypted S3 bucket — a GDPR violation waiting to happen."
> "KMS gives you the keys to your own kingdom. AWS cannot decrypt your data without your permission."

---

## Self-Quiz
1. What is envelope encryption?
2. Difference between SSE-S3 and SSE-KMS?
3. What does Macie detect and where?
4. What are the 4 S3 Block Public Access settings?
5. When would you use S3 Object Lock?
