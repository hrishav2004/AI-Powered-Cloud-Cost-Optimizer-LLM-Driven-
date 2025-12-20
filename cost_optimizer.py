import typer
from rich import print
from rich.prompt import Prompt

app = typer.Typer()

# 1. Extracts the structured project profile from CLI and write into project_description.txt file
@app.command()
def project_profile_extraction():
    desc = Prompt.ask("Enter the project description here")
    try:
        with open("project_description.txt", "a", encoding='utf-8') as f:
            f.write(desc)
            f.write("\n\n")
        print(f"[bold green]The project description has been successfully written into file![/bold green]")
    except Exception as e:
        print("\n[bold red]THE PROJECT DESCRIPTION COULD NOT BE EXTRACTED![/bold red]\n", e)

# 2. Generates realistic, budget-aware synthetic cloud-billing
@app.command()
def synthetic_billing_generation():
    print("Generating synthetic bill...")

# 3. Produces actionable cost optimization recommendations
@app.command()
def cost_optimization_recommendations():
    print("Recommending...")

# 4. Exports Reports
@app.command()
def export_reports():
    print("Exporting reports...")

@app.callback(invoke_without_command=True)
def main():
    print("""1. Enter a new project description:memo:\n2. Run Complete Cost Analysis:chart_with_upwards_trend::dollar:\n3. View Recommendations:bulb:\n4. Export Report:outbox_tray:""")
    choice = Prompt.ask("Choose the action you want to perform (1-4)")
    try:
        choice = int(choice)
        if choice not in [1,2,3,4]:
            raise Exception
        if choice == 1:
            project_profile_extraction()
        elif choice == 2:
            synthetic_billing_generation()
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