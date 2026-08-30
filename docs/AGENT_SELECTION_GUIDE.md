# Agent Architecture Selection Guide

This repository presents 23 architectural patterns. Choosing the right architecture for your task is a trade-off between **cost (tokens)**, **latency**, and **reliability**.

This guide will help you pick a starting point.

---

## 🚦 Quick Decision Tree

Answer these questions to find a recommended architecture:

1.  **Is the task simple and solvable in one step?** (e.g. classification)
    *   *Yes* → Use **Zero-Shot Prompting** (a plain LLM) or **Tool Use** (if external data is needed).
    *   *No* → Go to question 2.

2.  **Does code or text quality matter (do you need self-correction)?**
    *   *Yes* → **Reflection** (#01) or **Reflexive Metacognitive** (#17).

3.  **Does the task require a sequence of an unknown number of steps?**
    *   *Yes (e.g. web research)* → **ReAct** (#03).

4.  **Is the task complex but predictable (can you plan it up front)?**
    *   *Yes (e.g. writing a report)* → **Planning** (#04) or **PEV (Plan-Execute-Verify)** (#06) for reliability.

5.  **Do you need multiple different competencies (code + search + analysis)?**
    *   *Yes* → **Multi-Agent Systems** (#05) or **Meta-Controller** (#11).

6.  **Is the task mission-critical (errors are unacceptable)?**
    *   *Yes* → **Ensemble** (#13) for voting, or **Mental Loop** (#10) to simulate consequences.

7.  **Do you need to remember the user over a long period?**
    *   *Yes* → **Episodic + Semantic Memory** (#08).

---

## 📊 Architecture Comparison Matrix

| Architecture | Implementation complexity | Latency | Cost | Reliability | Best for... |
|:---|:---:|:---:|:---:|:---:|:---|
| **Reflection** | ⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Code generation, copywriting, translation |
| **Tool Use** | ⭐ | ⭐ | ⭐ | ⭐⭐ | Simple answers that need external data |
| **ReAct** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | Research, Q&A |
| **Planning** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | Document generation, multi-step tasks |
| **Multi-Agent** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Software development, complex analysis |
| **PEV** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Action automation, high-reliability operations |
| **Tree of Thoughts**| ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐| ⭐⭐⭐⭐⭐ | Complex logic, math, strategy |
| **Ensemble** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐| ⭐⭐⭐⭐⭐ | Decision-making, classification, fact-checking |

*(Scale: ⭐ = Low/Simple, ⭐⭐⭐⭐⭐ = High/Complex)*

---

## 🎯 Use Cases

### 1. High-quality code generation (Coding Assistant)
*   **Recommendation:** `Reflection` or `PEV`.
*   **Why:** A first draft often contains bugs. `Reflection` lets the model "look at" its own code via tests, and `PEV` (Plan-Execute-Verify) lets you run the code and check stderr before returning it.

### 2. Autonomous researcher (Research Agent)
*   **Recommendation:** `ReAct` with `Episodic Memory` or `Graph Memory`.
*   **Why:** The agent needs to follow links (`ReAct`). For deep research it needs to remember what it has already read (`Memory`) or build a knowledge map (`Graph`).

### 3. "Do-everything" enterprise assistant (General Assistant)
*   **Recommendation:** `Meta-Controller` (Router).
*   **Why:** User requests vary too widely. A router determines intent ("calculate the budget" vs. "write an email") and routes the task to either an accounting agent or a writing agent.

### 4. Financial analyst / trading (High Stakes)
*   **Recommendation:** `Ensemble` + `Mental Loop`.
*   **Why:** You can't rely on a single model's opinion. Run 3 different prompts (`Ensemble`) and average the forecast. Before executing a trade, simulate it with `Mental Loop`.

### 5. Solving logic puzzles
*   **Recommendation:** `Tree of Thoughts`.
*   **Why:** Solutions require exploring alternatives ("if I go left, then..."). Linear thinking loses out to tree-structured search here.

---

## 🛡️ Safety Patterns

For any architecture running in production, consider adding these protective layers:
*   **Human-in-the-loop (Dry Run #14):** Mandatory for state-changing actions (writing to a database, sending an email).
*   **Guardrails:** Input and output validation.

---
*Use this guide as a starting point, but always test architectures against your own specific data.*
