import typer
from rich import print
from rich.prompt import Prompt

from utils.LLMCalls.generate_project_profile import generate_project_profile
from utils.LLMCalls.generate_mock_billing import generate_mock_billing
from utils.LLMCalls.generate_cost_optimization_report import generate_cost_optimization_report

# Generates realistic, budget-aware, cloud-agnostic cost optimization report
def run_cost_analysis():
    print("[bold]Running cost analysis, this might take a few minutes...[/bold]")
    generate_project_profile()
    generate_mock_billing()
    generate_cost_optimization_report()
    print("[bold green]Cost analysis is complete![/bold green]")