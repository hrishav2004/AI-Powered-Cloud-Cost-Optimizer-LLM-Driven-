import typer
from rich import print
from rich.prompt import Prompt

from utils.LLMCalls.generate_project_profile import generate_project_profile

# Generates realistic, budget-aware synthetic cloud-billing
def run_cost_analysis():
    print("Running cost analysis, this might take a few minutes...")
    generate_project_profile()