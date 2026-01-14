import os
from typing import List, Optional
from dotenv import load_dotenv
from rich.console import Console

def setup_environment(project_name: str, required_keys: Optional[List[str]] = None) -> Console:
    """
    Sets up the environment for the notebooks:
    1. Loads environment variables from .env file.
    2. Sets up LangSmith tracing.
    3. Checks for required API keys.
    4. Returns a Rich Console for printing.
    """
    # Load .env from parent directory (assuming notebook is in the notebooks/ folder)
    # Adjust path if notebooks are nested deeper or moved
    load_dotenv(dotenv_path="../.env")
    
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = project_name
    
    console = Console()
    
    if required_keys:
        missing_keys = [key for key in required_keys if key not in os.environ]
        if missing_keys:
            console.print(f"[bold red]Warning:[/bold red] Missing environment variables: {', '.join(missing_keys)}")
            console.print("Please create a .env file in the project root with these keys.")
    else:
        # Default check for Nebius and LangChain as they are used almost everywhere
        if not os.environ.get("NEBIUS_API_KEY"):
             console.print("[yellow]Warning:[/yellow] NEBIUS_API_KEY not found.")
        if not os.environ.get("LANGCHAIN_API_KEY"):
             console.print("[yellow]Warning:[/yellow] LANGCHAIN_API_KEY not found.")

    console.print(f"[green]Environment setup for '{project_name}' complete.[/green]")
    return console
