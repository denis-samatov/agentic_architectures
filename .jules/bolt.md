## 2026-01-23 - IPython Import Overhead & Env Loading Patterns
**Learning:** `from IPython.display import ...` takes ~0.5s, which is significant for CLI/utility scripts. `load_dotenv` handles existence checks internally, making explicit `os.path.exists` checks redundant and potentially buggy if not mirrored exactly.
**Action:** Use lazy imports for heavy libraries like IPython. Rely on `load_dotenv` return value for control flow instead of pre-checks.
