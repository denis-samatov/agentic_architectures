## 2026-01-23 - IPython Import Overhead & Env Loading Patterns
**Learning:** `from IPython.display import ...` takes ~0.5s, which is significant for CLI/utility scripts. `load_dotenv` handles existence checks internally, making explicit `os.path.exists` checks redundant and potentially buggy if not mirrored exactly.
**Action:** Use lazy imports for heavy libraries like IPython. Rely on `load_dotenv` return value for control flow instead of pre-checks.

## 2026-01-24 - Rich Import & Remote Graph Rendering Latency
**Learning:** Importing `rich` adds ~0.3s overhead. `langgraph.draw_mermaid_png()` uses a remote API (Mermaid Ink), which is slower than local `pygraphviz`.
**Action:** Lazy import `rich` components. Prioritize local `draw_png()` over remote rendering methods in visualization utilities.
