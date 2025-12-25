import typer
from rich import print
from rich.prompt import Prompt

# Extracts the structured project profile from CLI and writes into project_description.txt file
def get_project_description():
    desc = Prompt.ask("Enter the project description here")
    try:
        with open("pipeline_output/project_description.txt", "w", encoding='utf-8') as f:
            f.write(desc)
        print(f"[bold green]The project description has been successfully written into file![/bold green]")
    except Exception as e:
        print("\n[bold red]THE PROJECT DESCRIPTION COULD NOT BE EXTRACTED![/bold red]\n", e)