## 2024-05-22 - Graceful Graph Visualization Fallback
**Learning:** In technical notebooks, complex visualizations (like LangGraph diagrams) often fail due to missing system dependencies (PyGraphviz). Users are left with ugly error traces.
**Action:** Implement a tiered fallback strategy: Try best visual (Mermaid API) -> Try local visual (PyGraphviz) -> Fallback to raw syntax (Mermaid text) for copy-pasting. This ensures the user *always* gets the information, even if the "pretty" version fails.
