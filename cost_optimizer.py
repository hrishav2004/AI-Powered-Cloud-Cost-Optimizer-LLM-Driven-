import typer, json, jsonschema
from rich import print
from rich.prompt import Prompt
from jsonschema import validate

# import all CLI command functions
from utils.get_project_description import get_project_description
from utils.run_cost_analysis import run_cost_analysis
from utils.cost_optimization_recommendations import cost_optimization_recommendations
from utils.export_reports import export_reports

app = typer.Typer()

@app.callback(invoke_without_command=True)
def main():
    print("""1. Enter a new project description:memo:\n2. Run Complete Cost Analysis:chart_with_upwards_trend::dollar:\n3. View Recommendations:bulb:\n4. Export Report:outbox_tray:\n5. Exit:door:🏃""")
    choice = Prompt.ask("Choose the action you want to perform (1-5)")
    try:
        choice = int(choice)
        if choice not in [1,2,3,4,5]:
            raise Exception
        if choice == 1:
            get_project_description()
            main()
        elif choice == 2:
            run_cost_analysis()
            main()
        elif choice == 3:
            cost_optimization_recommendations()
            main()
        elif choice == 4:
            export_reports()
            main()
        else:
            pass
    # Catches exceptions, when the project_description.txt file doesn't exist
    except FileNotFoundError as e:
        print(e)
        print("\n[bold red]There doesn't exist any project_description.txt file![/bold red]\n")
        main()
    # Catches exceptions when the json schema is not valid
    except jsonschema.exceptions.ValidationError as e:
        print(f"\n[bold red]Report generation failed![/bold red]\n[blue]Validation error details: {e}[/blue]\n")
        main()
    # Catches exceptions, when the user enters a value other than 1,2,3,4 or some other invalid/non-numeric string
    except Exception as e:
        print(e)
        print(f"\n[bold red]PLEASE ENTER A VALID CHOICE BETWEEN 1-4![/bold red]\n")
        main()
    

if __name__ == "__main__":
    app()