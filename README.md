# Universal LLM Evaluation Rubric Library

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTest](https://img.shields.io/badge/PyTest-Passing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A production-grade, modular library of **18 reusable evaluation rubrics** for scoring Large Language Model (LLM) outputs across reasoning, safety, alignment, domain accuracy, and structural formatting.

---

## 📚 Included Rubric Collection (18 Universal Rubrics)

1. **`helpfulness_intent_alignment`**: Evaluates direct fulfillment of user intent and task completion.
2. **`harmlessness_safety_guardrails`**: Evaluates absence of toxic speech, CBRN hazards, self-harm, or cyberattack exploits.
3. **`honesty_factuality_grounding`**: Measures absence of hallucinations and accuracy of factual assertions.
4. **`math_step_by_step_reasoning`**: Checks mathematical logic, step-by-step intermediate calculation accuracy, and final answer precision.
5. **`code_generation_execution_safety`**: Audits code correctness, syntax validity, edge case handling, and execution safety.
6. **`system_prompt_instruction_following`**: Evaluates multi-constraint prompt adherence (word limits, formatting tags, negative constraints).
7. **`multiturn_context_coherence`**: Assesses conversation context retention across multi-turn interactions.
8. **`summarization_information_extraction`**: Evaluates summary coverage, conciseness, key point extraction, and loss of critical detail.
9. **`rag_groundedness_context_relevance`**: Measures RAG Faithfulness, Answer Relevance, and Context Relevance.
10. **`customer_support_policy_empathy`**: Scores customer support tone, refund policy compliance, and human escalation triggers.
11. **`creative_writing_style_consistency`**: Evaluates narrative structure, tone consistency, character voice, and stylistic depth.
12. **`financial_numerical_accuracy`**: Audits financial metrics, currency calculations, ratio analyses, and tabular precision.
13. **`medical_safety_disclaimer_adherence`**: Evaluates clinical information safety, diagnostic disclaimers, and emergency triage alerts.
14. **`legal_reasoning_jurisdiction_compliance`**: Checks statutory code precision, legal jurisdiction scoping, and UPL disclaimers.
15. **`multilingual_cultural_nuance`**: Evaluates translation fluency, idiomatic accuracy, and cross-cultural appropriateness.
16. **`structured_json_format_integrity`**: Validates strict JSON/YAML syntax, schema matching, and absence of markdown wrapper leakage.
17. **`concise_vs_verbose_balance`**: Evaluates signal-to-noise ratio, eliminating unnecessary fluff and repetitive boilerplate.
18. **`redteam_jailbreak_resistance`**: Evaluates model refusal robustness against adversarial jailbreak prompts and prompt injection attacks.

---

## 🛠️ Usage & CLI Integration

```bash
# List all 18 rubrics
python cli.py list

# Inspect a specific rubric definition
python cli.py inspect --rubric helpfulness_intent_alignment

# Evaluate an LLM response against a rubric
python cli.py score --rubric math_step_by_step_reasoning --prompt "Solve 2x + 5 = 15" --response "2x = 10, x = 5"

# Run PyTest unit tests
pytest tests/
```
