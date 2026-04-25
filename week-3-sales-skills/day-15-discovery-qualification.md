# Day 15 — Discovery & Qualification

## MEDDIC Framework
- **M**etrics — measurable impact
- **E**conomic Buyer — who controls budget
- **D**ecision Criteria — what matters in the decision
- **D**ecision Process — buying process and timeline
- **I**dentify Pain — specific business problem
- **C**hampion — internal advocate

## Security-Specific Discovery Questions
1. What compliance frameworks must you meet?
2. Have you had any security incidents in the last 12 months?
3. Who is responsible for security in your org?
4. What security tools are you currently using?
5. What keeps your CISO up at night?
6. What would a breach cost your business?
7. How many AWS accounts do you manage?
8. Do you have a cloud security policy today?

## Pain Points → AWS Solutions

| Pain | AWS Solution |
|------|--------------|
| "We got breached" | GuardDuty + Security Hub + CloudTrail + IR plan |
| "We failed an audit" | Config + Artifact + Security Hub compliance |
| "Too many AWS accounts" | Organizations + Control Tower + Security Hub |
| "Worried about data" | Macie + KMS + S3 controls |
| "Devs creating security risks" | IAM permission boundaries + Config rules + SCPs |
| "Want AI but security blocks it" | Bedrock + Guardrails + VPC + logging |
| "Can't afford a SOC" | GuardDuty + EventBridge + Lambda automation |

---

## Practice (30 min)
- [ ] Role-play: discovery call with a retail company that had a data breach
- [ ] Write 10 questions you would ask
