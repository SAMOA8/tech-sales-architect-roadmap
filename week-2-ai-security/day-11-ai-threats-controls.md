# Day 11 — AI Security: Threats, Risks & Controls

> **This is your biggest differentiator.** Most Sales Architects don't know this material.

## AI-Specific Security Threats

### Prompt Injection (most critical)
- **Direct** — user manipulates AI ("Ignore previous instructions...")
- **Indirect** — malicious content in docs the AI reads
- Defense: Bedrock Guardrails, input validation, separation of user/system prompts

### Other Threats
- **Model Inversion** — reverse-engineer training data
- **Data Poisoning** — corrupt training data (backdoor attacks, label flipping)
- **Model Stealing** — query API to recreate model
- **Hallucination Risk** — confident but wrong info (high-stakes decisions)
- **Insecure Plugin/Tool Use** — AI agents calling APIs unsafely
- **Excessive Agency** — AI given too many permissions
- **Training Data Privacy** — sensitive data in training sets

## OWASP LLM Top 10 (memorize this list)
1. Prompt Injection
2. Insecure Output Handling
3. Training Data Poisoning
4. Model Denial of Service
5. Supply Chain Vulnerabilities
6. Sensitive Information Disclosure
7. Insecure Plugin Design
8. Excessive Agency
9. Overreliance
10. Model Theft

## AI Security Controls

### Bedrock Guardrails
- Content filtering (toxic, harmful, hateful)
- Denied topics (e.g., never discuss competitor products)
- Word filters
- PII redaction (auto-detect and mask)
- Grounding checks (responses based on KB)

### Other Controls
- **Bedrock Invocation Logging** — log all I/O for audit
- **IAM for Bedrock** — control which users/roles call which models
- **VPC for Bedrock** — private connectivity, no internet exposure
- Rate limiting via WAF
- Token consumption monitoring

---

## Practice (30 min)
- [ ] "Customer wants HR chatbot handling employee data. What security controls?"
- Answer: Guardrails (PII redaction), IAM, VPC, Invocation Logging, data classification

---

## Self-Quiz
1. Direct vs indirect prompt injection?
2. Name 5 OWASP LLM Top 10 risks.
3. What does Bedrock Guardrails protect against?
4. How do you prevent model theft?
5. What is Excessive Agency and how do you prevent it?
