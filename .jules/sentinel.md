## 2024-10-26 - Prompt Injection in Security Guardrails
**Vulnerability:** The security guardrail implementation (`notebooks/23_constitutional_guardrails.ipynb`) interpolated user input directly into the LLM prompt using f-strings without any delimiters.
**Learning:** Even code designed to enforce security (guardrails) is susceptible to basic injection attacks if it fails to distinguish between "instructions" and "data". A clever user could override the "Constitution" by injecting conflicting instructions.
**Prevention:** Treat all user input as untrusted data. Use XML tags (e.g., `<user_request>...</user_request>`) or separate System/User message roles to clearly demarcate input from logic.
