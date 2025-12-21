import typer
from rich import print
from rich.prompt import Prompt

from .generate_project_profile import generate_project_profile

# Extracts the structured project profile from CLI, writes into project_description.txt file and converts it into project_profile.json via LLM call
def get_project_description():
    desc = Prompt.ask("Enter the project description here")
    try:
        with open("project_description.txt", "w", encoding='utf-8') as f:
            f.write(desc)
        print(f"[bold green]The project description has been successfully written into file![/bold green]")
        generate_project_profile()
    except Exception as e:
        print("\n[bold red]THE PROJECT DESCRIPTION COULD NOT BE EXTRACTED![/bold red]\n", e)