# Agentic System Evaluation Framework

Evaluating AI agents is one of the hardest problems in LLM application development. Unlike traditional software, where tests are binary (pass/fail), agents are non-deterministic and "quality" criteria are often subjective.

This document describes the methodology and metrics for building a reliable evaluation pipeline for your agents.

---

## 1. Five levels of evaluation

We recommend a multi-tiered testing approach, from cheap automated checks to qualitative human evaluation.

### Level 1: Syntactic validation (Unit Tests)
Checks that the agent returns data in the correct format.
*   **What we check:** Is the JSON valid? Does the Pydantic model parse? Does the code compile?
*   **Cost:** 🟢 Very low.
*   **Tools:** `assert`, `try/except`, `pydantic`.

### Level 2: Deterministic metrics (Deterministic Assertions)
Fact-checking when the correct answer is known exactly.
*   **What we check:** Does the answer contain a keyword? Does the numeric answer match the gold standard? Was the tool called with the expected arguments?
*   **Cost:** 🟢 Very low.
*   **Metrics:** Exact Match, String Inclusion, RegEx.

### Level 3: Semantic evaluation (Embedding Distance)
Comparing the meaning of an answer to a reference answer without requiring an exact word match.
*   **What we check:** How close is the agent's answer vector to the correct answer's vector?
*   **Cost:** 🟡 Medium.
*   **Metrics:** Cosine Similarity.

### Level 4: LLM-as-a-Judge 🏆
Using a strong model (e.g. GPT-4o) to evaluate the output of a weaker or specialized model.
*   **What we check:** Helpfulness, politeness, safety, hallucinations, coherence.
*   **Cost:** 🔴 High.
*   **Tools:** Custom judge prompts, Ragas, DeepEval.

### Level 5: Human evaluation (HumanEval / ELO)
The gold standard, but the most expensive and slowest.
*   **What we check:** Subtle nuances, creativity, "human-ness."
*   **Cost:** 🔴🔴🔴 Very high.

---

## 2. Key metrics

When evaluating agents, focus on three dimensions:

### A. Result quality
1.  **Correctness:** Did the agent answer the question correctly given the context?
2.  **Faithfulness:** Is the answer grounded only in the provided context (retrieval), or did the agent invent facts (hallucination)?
3.  **Relevance:** How well does the answer match the user's request (no filler).

### B. Agent efficiency
1.  **Trajectory Validity:** Were the agent's steps logical? Did it loop in circles?
2.  **Tool Selection Accuracy:** Did the agent pick the right tool for the task?
3.  **Tool Argument Quality:** Did it pass the tool the correct parameters?

### C. Safety and style
1.  **Maliciousness:** Did the agent attempt to follow malicious instructions (jailbreak)?
2.  **Tone Consistency:** Does the tone match the assigned persona?

---

## 3. The LLM-as-a-Judge pattern

Most notebooks in this project use the "Judge" pattern. This is a prompt that receives as input:
1.  `Input`: the user's request.
2.  `Output`: the agent's answer.
3.  `Context` (optional): the tools or documents used.
4.  `Reference` (optional): the ideal answer.

### Example judge prompt (G-Eval style):

```text
You are an impartial AI judge. Your task is to evaluate the quality of an AI
assistant's answer based on the following criterion:

Criterion: HELPFULNESS
Score: 1 to 5
1 - The answer is completely unhelpful or incorrect.
3 - The answer is helpful but contains unnecessary information or misses details.
5 - A perfect, concise, and accurate answer.

User Input: {input}
AI Output: {output}

Explain your reasoning step by step, then output the score in the format: [[SCORE]].
```

---

## 4. Building an evaluation pipeline

For a professional project you need an **Evaluation Dataset**.

1.  **Build a golden dataset:**
    *   20-50 `(Question, Ideal Answer)` pairs.
    *   Include "hard" cases (adversarial examples).
2.  **Run a sweep:**
    *   Run the questions through your agent.
    *   Save the "trajectories" (intermediate steps) and final answers.
3.  **Run the judge:**
    *   Compare the agent's answers to the ideal answers using an LLM judge.
4.  **Analyze the report:**
    *   If score < 4/5 → analyze the trajectories. Where did the agent go wrong?
        *   Wrong tool? → Improve the `Tool Description`.
        *   Confused reasoning? → Improve the `Reasoning Prompt` or switch models.

---

## 5. Ecosystem tools

You don't need to build everything from scratch. Industry standards:
*   **LangSmith (LangChain):** The best tool for tracing and evaluating chains.
*   **Ragas:** A framework specifically for evaluating RAG (relevance, faithfulness).
*   **DeepEval:** Unit tests for LLMs.
*   **Arize Phoenix:** An open-source alternative for tracing and evaluation.
