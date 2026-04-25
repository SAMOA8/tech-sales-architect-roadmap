# Day 6 — Identity Services: SSO, Cognito, Organizations

## AWS IAM Identity Center (formerly AWS SSO)
- SSO across all AWS accounts and business apps
- Integrates with: Microsoft AD, Okta, Azure AD/Entra ID, Google Workspace
- **Permission sets** — define what users can do in each account
- Critical for enterprises managing 10+ AWS accounts

## AWS Organizations
- Centralized multi-account management
- **OUs (Organizational Units)** — logical grouping (Production, Dev, Sandbox)
- **SCPs (Service Control Policies)** — guardrails (set MAX permissions, do NOT grant)
- Consolidated billing, volume discounts
- **AWS Control Tower** — automated landing zone with guardrails

## Amazon Cognito (1 hour)
- User auth & authz for web/mobile apps (your customers, not employees)
- **User Pools** — sign-up/sign-in directory (username/password, MFA, social, SAML, OIDC)
- **Identity Pools** — temporary AWS credentials for users → IAM roles
- Returns JWT tokens (ID, Access, Refresh)

## AWS Secrets Manager
- Secret storage with auto-rotation (DB creds, API keys)
- Integrates with RDS for password rotation
- Compare to **Parameter Store** (free, simpler, less rotation)

---

## Practice (30 min)
- [ ] Write: "A customer has 50 AWS accounts across 5 teams. How do you help them centralize access?"
- [ ] Answer should mention: Organizations + OUs + IAM Identity Center + SCPs

---

## Sales Talking Points
> "Cognito for customers, IAM for employees, Identity Center for federated AWS access — one identity story across your entire stack."
> "SCPs are your guardrails. Even an admin in an account can't disable CloudTrail if the SCP forbids it."

---

## Self-Quiz
1. Cognito vs IAM — when do you use each?
2. User Pool vs Identity Pool?
3. What is an SCP and why does it differ from an IAM policy?
4. What problem does AWS Control Tower solve?
5. Secrets Manager vs Parameter Store — when to use each?
