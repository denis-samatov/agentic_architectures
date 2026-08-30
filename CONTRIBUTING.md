# Contributing to All Agentic Architectures

Thanks for your interest in the project! We welcome any help — from fixing typos to adding new architectures.

## 🚀 Getting started

1.  **Fork the repository** and clone it locally.
2.  **Set up your environment**:
    ```bash
    make install
    ```
    This creates a virtual environment and installs dependencies.
3.  **Create an .env file**:
    ```bash
    cp .env.example .env
    # Fill in your API keys
    ```

## 🛠 Development process

-   Add new notebooks to the `notebooks/` folder.
-   Follow the existing file numbering (e.g. `18_new_architecture.ipynb`).
-   Before submitting changes, make sure the code is formatted and linted.

## 📝 Code style

We use `ruff` for linting and formatting.
```bash
make lint
make format
```

## 🐛 Reporting bugs

If you find a bug, please open an Issue with a detailed description of the problem and steps to reproduce it.
