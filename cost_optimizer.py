import typer
from rich import print
from rich.prompt import Prompt

# import all CLI command functions
from utils.get_project_description import get_project_description
from utils.run_cost_analysis import run_cost_analysis
from utils.cost_optimization_recommendations import cost_optimization_recommendations
from utils.export_reports import export_reports

app = typer.Typer()

@app.callback(invoke_without_command=True)
def main():
    print("""1. Enter a new project description:memo:\n2. Run Complete Cost Analysis:chart_with_upwards_trend::dollar:\n3. View Recommendations:bulb:\n4. Export Report:outbox_tray:""")
    choice = Prompt.ask("Choose the action you want to perform (1-4)")
    try:
        choice = int(choice)
        if choice not in [1,2,3,4]:
            raise Exception
        if choice == 1:
            get_project_description()
        elif choice == 2:
            run_cost_analysis()
        elif choice == 3:
            cost_optimization_recommendations()
        else:
            export_reports()
    # Catches exceptions, when the user enters a value other than 1,2,3,4 or some other invalid/non-numeric string
    except Exception as e:
        print(f"\n[bold red]PLEASE ENTER A VALID CHOICE BETWEEN 1-4![/bold red]\n")
        main()
    

if __name__ == "__main__":
    app()