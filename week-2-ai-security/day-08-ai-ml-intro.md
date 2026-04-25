# Day 8 — Introduction to AI/ML on AWS

## Three Layers of AI on AWS
1. **AI Services** (pre-built): Rekognition, Comprehend, Polly, Transcribe — no ML knowledge needed
2. **ML Platform**: SageMaker — build/train/deploy custom models
3. **Foundation Models**: Bedrock — Claude, Llama, Titan, Mistral

## Key AI Terms to Know Cold
- **LLM** — Large Language Model
- **Foundation Model (FM)** — base model fine-tunable for specific tasks
- **Inference** — running a trained model
- **Fine-tuning** — training base model on your data
- **RAG** — Retrieval Augmented Generation; LLM + your knowledge base
- **Prompt engineering** — crafting inputs for better outputs
- **Hallucination** — AI generating confident but incorrect info
- **Token** — ~4 characters; models charge per token

## AWS AI Services
- **Rekognition** — image/video analysis (face, objects, content moderation)
- **Comprehend** — NLP (sentiment, entities, PII detection)
- **Comprehend Medical** — HIPAA-eligible medical NLP
- **Textract** — extract text/forms/tables from docs
- **Transcribe** — speech-to-text
- **Polly** — text-to-speech
- **Translate** — language translation
- **Forecast** — time-series forecasting
- **Personalize** — recommendations engine
- **Lookout for Metrics** — anomaly detection in business metrics

---

## Practice (30 min)
- [ ] "Which AWS AI service for a bank wanting to extract data from loan applications?"
- Answer: Textract + Comprehend (PII detection)

---

## Self-Quiz
1. What's the difference between an LLM and a Foundation Model?
2. What is RAG and why does it matter?
3. Which service detects PII in plain text documents?
4. What is a token in AI?
5. Comprehend vs Comprehend Medical?
