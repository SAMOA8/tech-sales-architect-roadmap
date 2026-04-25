# Day 3 — Network Security: VPC, WAF, Shield, CloudFront

## VPC Security (1 hour)
- VPC = isolated virtual network in AWS
- **Public subnet** — route to Internet Gateway
- **Private subnet** — no direct internet, uses NAT Gateway for outbound
- **Security Groups** — stateful, instance-level, allow rules only
- **NACLs** — stateless, subnet-level, allow + deny, ordered rules
- **VPC Flow Logs** — traffic metadata to CloudWatch/S3
- **VPC Peering** — private connectivity, no transitive routing
- **VPN** — encrypted IPsec tunnel over internet
- **Direct Connect** — dedicated private line (high bandwidth, low latency, higher cost)
- **VPC Endpoints** — private connection to AWS services without internet
- **PrivateLink** — private SaaS service connectivity

## Edge Security (1 hour)

### AWS WAF (Web Application Firewall)
- Protects against OWASP Top 10: SQLi, XSS, CSRF
- Web ACLs with rules: allow / block / count / CAPTCHA
- Managed rule groups (AWS, marketplace)
- Deploys on: CloudFront, ALB, API Gateway, AppSync
- Rate limiting

### AWS Shield
- **Standard** — free, automatic, layer 3/4 DDoS for all customers
- **Advanced** — paid (~$3000/month), layer 7 DDoS, real-time metrics, financial protection, 24/7 DRT support
- Recommend Advanced for: revenue-critical apps, public web apps, customer-facing APIs

### AWS Firewall Manager
- Centrally manages WAF, Shield, Security Groups across all Org accounts
- Critical for enterprises with 50+ accounts

---

## Practice (30 min)
- [ ] Sketch a VPC architecture: public subnet, private subnet, NAT Gateway, IGW
- [ ] Practice explaining it to someone non-technical

---

## Sales Talking Points
> "Without WAF, your web app is exposed to bots and injection attacks 24/7. Managed rule groups stop the OWASP Top 10 in 5 minutes of setup."
> "Shield Advanced pays for itself — one major DDoS can cost more in downtime than a year of Shield fees."

---

## Self-Quiz
1. Difference between Security Group and NACL (4 differences)?
2. When would you choose Direct Connect over VPN?
3. What does WAF protect against that Shield does not?
4. What is Shield Advanced's "financial protection"?
5. When would you recommend AWS Firewall Manager?
