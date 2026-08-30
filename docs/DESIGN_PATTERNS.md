# Agentic System Design Patterns

Professional agent development is like building with blocks. You don't write an agent "from scratch" — you combine known, time-tested patterns.

This document systematizes the core structural blocks and control-flow patterns used throughout the project.

---

## 1. Structural Patterns

How the agent's "brain" itself is organized.

### 🎭 Persona / Role Pattern
Assigning the agent a specific role to narrow its search space and set its style.
*   **Example:** "You are a senior Python developer. You write code following PEP8, prefer composition over inheritance..."
*   **Why:** Improves the specificity and quality of answers in narrow domains.

### 🗣️ Chain of Thought (CoT)
Prompting the model to "think out loud" before answering.
*   **Implementation:** Adding an instruction like `Let's think step by step` to the prompt, or explicitly requiring a `Thought: ... Action: ...` structure.
*   **Why:** Significantly improves the model's ability to solve logical and mathematical problems.

### 💉 Few-Shot Prompting
Providing the model with "Question -> Answer" examples inside the context window.
*   **Implementation:** Dynamic Few-Shot — selecting examples from a vector store that are most similar to the current user query.
*   **Why:** Sets the output format and solution logic without fine-tuning the model's weights.

---

## 2. Control Flow Patterns

How information moves through the system (typically implemented via graphs, e.g. LangGraph).

### 🔗 Chain
A linear sequence of steps.
*   `Input -> Step 1 -> Step 2 -> Output`
*   **Example:** Fetch text -> Summarize -> Translate.

### 🔄 Loop / Cycle
Repeating steps until an exit condition is met. The foundation of agency.
*   **Refinement Loop:** Generate -> Check -> If it's bad, generate again.
*   **ReAct Loop:** Thought -> Tool -> Observation -> Thought...

### 🔀 Routing
Classifying a request and directing it down different paths.
*   **Example:** If the question is about pricing -> a database agent. If it's about policy -> a knowledge-base agent (RAG).
*   **Technique:** Use `llm.with_structured_output` for reliable intent classification.

### 🔠 Parallelization (Fan-out / Fan-in)
Running independent tasks concurrently, then aggregating the results.
*   **Sectioning:** Write different sections of a report in parallel.
*   **Voting:** Ask 3 different models and pick the most popular answer (Self-Consistency).

---

## 3. Reliability Patterns

How to make the system resilient to failures.

### 🛡️ Guardrails
Syntactic or semantic filters on input and output.
*   **Input Rail:** Checking whether the user is attempting to jailbreak the system (prompt injection).
*   **Output Rail:** Checking whether the model is leaking PII (personal data) or producing invalid JSON. If the check fails, return an error or regenerate.

### 🏃‍♂️ Fallback
A "plan B" for when the primary mechanism fails.
*   **Example:** If the `GoogleSearch` tool call times out, fall back to `WikipediaSearch`. If GPT-4 returns an API error, switch to GPT-3.5 or Claude.

### 👁️ Human-in-the-Loop
Pausing graph execution to get approval or edits from a human.
*   **Pattern:** `Plan -> (Wait for Approval) -> Execute`.
*   **Implementation:** Use LangGraph's `interrupt_before` or checkpoint mechanisms.

---

## 4. Memory Patterns

### 🧠 Short-term Memory (Window Buffer)
Storing only the last N messages. Cheap and simple, but loses context in long conversations.

### 🗄️ Summary Memory
Periodically summarizing older messages. Lets you retain the gist of a conversation indefinitely, at the cost of detail.
*   **Implementation:** A background process that compresses `Messages[0:N]` into a `SystemMessage("Earlier we discussed...")`.

### 🗂️ CRUD Memory (Shared State)
Using external storage (a database) as a "sheet of paper."
*   The agent can explicitly `Read`, `Update`, `Delete` records about the user. This lets facts change ("the user moved to Berlin") without losing prior context.

---
*When designing your own systems, combine these patterns. For example, a **ReAct** agent might use **Few-Shot** prompting and have **Memory** with **Fallback** mechanisms.*
