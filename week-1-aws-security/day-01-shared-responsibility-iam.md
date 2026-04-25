# Day 1 — AWS Shared Responsibility Model & IAM Deep Dive

## Concepts (1 hour)

### AWS Shared Responsibility Model
- **AWS secures:** hardware, hypervisor, global infrastructure, managed service runtime
- **You secure:** OS, apps, data, IAM, network config
- For managed services (RDS, Lambda, Bedrock), AWS takes more responsibility — but customer still owns IAM, encryption keys, network placement

### Why this matters in sales
- Customers often assume AWS handles all security — correcting this opens the door to selling KMS, GuardDuty, Security Hub
- Compliance: customer is always responsible for their data and access controls regardless of cloud provider

---

## IAM Deep Dive (1 hour)

### IAM Components
- **User** — individual with long-term credentials
- **Group** — collection of users; assign policies to groups
- **Role** — temporary identity assumed by services or federated users
- **Policy** — JSON Allow/Deny rules on Actions/Resources

### Best Practices to Memorize
- MFA on all accounts (root especially)
- Never use root for daily work
- Apply least privilege
- Rotate access keys regularly
- Use Roles, not access keys, for EC2

### Advanced Concepts
- **Permission boundaries** — cap maximum permissions for a user/role
- **SCPs (Service Control Policies)** — Organization-level guardrails
- **Identity Federation** — SAML, OIDC, AD integration via IAM Identity Center

---

## Practice (30 min)

- [ ] Log into AWS Console, navigate IAM
- [ ] Create a test IAM user, attach policy, then delete
- [ ] Write 3 sentences explaining IAM to a non-technical customer

---

## Sales Talking Points

> "AWS gives you 99.99% infrastructure uptime — but your team controls who has access. That's where most breaches actually happen."

> "IAM is your first line of defense, and most customers underestimate how complex it gets at scale with hundreds of accounts and thousands of users."

---

## Self-Quiz
1. What is the Shared Responsibility Model in one sentence?
2. Difference between an IAM Role and an IAM User?
3. What is a permission boundary and when is it used?
4. Difference between an SCP and an IAM policy?
5. Why should the root account never have access keys?
