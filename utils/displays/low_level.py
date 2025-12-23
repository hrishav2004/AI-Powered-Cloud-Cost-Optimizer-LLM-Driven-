import typer
import pandas as pd
from rich import print

app = typer.Typer()

def display(curr, total_savings):
    color_map = {
        "compute": "blue",
        "database": "magenta",
        "storage": "cyan",
        "networking": "yellow",
        "monitoring": "green",
        "cache": "purple",
        "loadbalancer": "blue",
        "cdn": "blue",
        "logging": "grey",
        "backup": "slate",
        "low": "green",
        "medium": "yellow",
        "high": "red"
    }

    service, title, cost, savings, description, effort, risk, steps, cloud_providers = curr["Service"], curr["Title"], curr["Current Cost"], curr["Potential Savings"], curr["Description"], curr["Implementation Effort"], curr["Risk Level"], curr["Steps"], curr["Cloud Providers"]
    percentage_savings = round(savings/total_savings * 100, 1)
    if service.lower() in color_map:
        print(f"[bold] [{color_map[service.lower()]}]{service.upper()} • [/{color_map[service.lower()]}]{title}[/bold]")
    else:
        print(f"[bold]{service.upper()} • {title}[/bold]")
    print("\n")
    print("[slate]SUMMARY[/slate]")
    print(f"Current Cost: [bold white]\u20B9{cost}[/bold white]\nPotential Savings: [bold green]\u20B9{savings}(~{round(savings/cost * 100, 1)}%)[/bold green]\nPercent of total savings: [bold white]{percentage_savings}%[/bold white]\nEffort: [bold {color_map[effort.lower()]}]{effort}[/bold {color_map[effort.lower()]}]\nRisk: [bold {color_map[risk.lower()]}]{risk}[/bold {color_map[risk.lower()]}]")
    print("\n")
    print("DESCRIPTION")
    print(f"[italic]{description}[italic]")
    print("\n")
    print("STEPS")
    idx=1
    for step in steps:
        print(f"{idx}. {step}")
        idx+=1
    print("\n")
    print("CLOUD PROVIDERS")
    idx=1
    for provider in cloud_providers:
        print(f"{idx}. {provider}")
        idx+=1

@app.callback(invoke_without_command=True)
def low_level(df: pd.DataFrame):
    print("[bold]Please follow the given instructions to decide your next set of actions:[/bold]")
    print(f"[bold]Enter a number (1-{len(df)}) [blue]to view[/blue] details of the corresponding recommendation.[/bold]")
    print("[bold]Type 'q' to return to the main menu.[/bold]")

    choice = input("> ")
    try:
        choice = int(choice)
        if choice in range(1, len(df)+1):
            curr = df.loc[choice-1]
            total_savings = df["Potential Savings"].sum()
            display(curr, total_savings)
            print(f"")
            print("\n")
            low_level(df)
        else:
            print(f"\n[bold red]Please enter a number between 1 and {len(df)}![/bold red]\n")
            low_level(df)
    except ValueError as e:
        if choice == "q":
            pass
        else:
            print("\n[bold red]Please enter a valid input![/bold red]\n")
            low_level(df)

if __name__ == "__low_level__":
    app()