# AWS Security Audit Tool

A Python command-line tool that audits an AWS account for common security misconfigurations — aligned with the AWS Shared Responsibility Model and AWS security best practices.

> Built as part of my AWS Security training (Craw Security / FutureSkills Prime).

---

## What It Checks

| # | Check | Severity |
|---|-------|----------|
| 1 | Root account MFA enabled | Critical |
| 2 | No active root access keys | Critical |
| 3 | IAM password policy strength | High |
| 4 | IAM users with console access but no MFA | High |
| 5 | CloudTrail enabled and actively logging | High |
| 6 | S3 bucket Block Public Access (account + per bucket) | High |
| 7 | Security groups open to 0.0.0.0/0 on SSH (22) / RDP (3389) | High |
| 8 | GuardDuty enabled | Medium |
| 9 | AWS Config recorder active | Medium |
| 10 | Default VPC exists (attack surface reminder) | Low |

---

## Sample Output

```
============================================================
  AWS SECURITY AUDIT REPORT
  Generated: 2026-04-24 10:32:11 UTC
  Region:    us-east-1
============================================================
  [INFO] Authenticated as: arn:aws:iam::123456789012:user/demo-user

────────────────────────────────────────────────────────────
  Root Account Security
────────────────────────────────────────────────────────────
  [PASS] Root account MFA is enabled
  [PASS] No active root account access keys

────────────────────────────────────────────────────────────
  IAM Password Policy
────────────────────────────────────────────────────────────
  [FAIL] IAM password policy is weak:
      • minimum length is 8 (recommend >=14)
      • no password expiry set

────────────────────────────────────────────────────────────
  Security Group Exposure
────────────────────────────────────────────────────────────
  [FAIL] 1 security group rule(s) expose sensitive ports:
      • sg-0abc1234 (launch-wizard-1) — port 22 (SSH) open to 0.0.0.0/0

============================================================
  SUMMARY
============================================================
  [PASS] 5 check(s) passed
  [FAIL] 4 check(s) failed
  [WARN] 2 warning(s)

  Score: 5/9 checks passed
```

See [sample_output.txt](sample_output.txt) for the full example report.

---

## Prerequisites

- Python 3.8+
- An AWS account with an IAM user or role that has **read-only** permissions
- AWS CLI configured (`aws configure`) **or** environment variables set

### Minimum IAM Permissions Required

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:GetAccountSummary",
        "iam:GetAccountPasswordPolicy",
        "iam:ListUsers",
        "iam:GetLoginProfile",
        "iam:ListMFADevices",
        "cloudtrail:DescribeTrails",
        "cloudtrail:GetTrailStatus",
        "s3:ListAllMyBuckets",
        "s3:GetBucketPublicAccessBlock",
        "s3control:GetPublicAccessBlock",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeVpcs",
        "guardduty:ListDetectors",
        "guardduty:GetDetector",
        "config:DescribeConfigurationRecorders",
        "config:DescribeConfigurationRecorderStatus",
        "sts:GetCallerIdentity"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/aws-security-audit-tool.git
cd aws-security-audit-tool

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
# Audit using default AWS profile and us-east-1
python audit.py

# Specify a named AWS profile
python audit.py --profile my-profile

# Specify a different region
python audit.py --region eu-west-1

# Save the report to a file
python audit.py --output report.txt

# Combine options
python audit.py --profile prod --region ap-southeast-1 --output prod_report.txt
```

---

## AWS Credential Setup

**Option 1 — AWS CLI (recommended)**
```bash
aws configure
# Enter: Access Key ID, Secret Access Key, region, output format
```

**Option 2 — Environment variables**
```bash
export AWS_ACCESS_KEY_ID=your_key_id
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

> **Security note:** Never hard-code credentials in the script or commit them to Git. The `.gitignore` in this repo excludes credential files automatically.

---

## Project Structure

```
aws-security-audit-tool/
├── audit.py            # Main audit script
├── requirements.txt    # Python dependencies (boto3)
├── sample_output.txt   # Example output — no real account data
├── .gitignore          # Excludes credentials, venvs, cache
└── README.md           # This file
```

---

## Concepts Covered

This project demonstrates practical application of topics from AWS Security training:

- **Module 01** — AWS Shared Responsibility Model (what AWS vs. customer secures)
- **Module 02** — IAM: users, MFA, password policies, root account hardening
- **Module 03** — VPC: default VPC risk, security group exposure
- **Module 05** — EC2 security: SSH/RDP exposure via security groups
- **Module 07/08** — CloudTrail logging, GuardDuty, AWS Config

---

## Remediation Guide

| Finding | How to Fix |
|---------|-----------|
| Root MFA not enabled | AWS Console → IAM → Security credentials → Activate MFA |
| Root access keys exist | IAM → Security credentials → Delete access keys |
| Weak password policy | IAM → Account settings → Edit password policy |
| IAM user no MFA | IAM → Users → [user] → Security credentials → Assign MFA |
| CloudTrail not logging | CloudTrail → Trails → Create trail or enable logging |
| Public S3 bucket | S3 → [bucket] → Permissions → Block Public Access → Edit |
| SSH/RDP open to 0.0.0.0/0 | EC2 → Security Groups → Edit inbound rules → restrict to specific IP |
| GuardDuty not enabled | GuardDuty → Get started → Enable |
| AWS Config not recording | AWS Config → Settings → Turn on recording |
| Default VPC exists | VPC → Your VPCs → Delete default VPC (if unused) |

---

## Future Improvements

- [ ] Multi-region scanning (scan all enabled regions at once)
- [ ] HTML report output
- [ ] Checks for KMS key rotation (Module 04)
- [ ] Amazon Macie S3 sensitive data findings
- [ ] Export findings in JSON format for SIEM integration
- [ ] GitHub Actions workflow for scheduled automated scans

---

## Author

**Samoa Shang**
AWS Security Training — Craw Security / FutureSkills Prime

---

## License

MIT License — free to use, modify, and distribute.
