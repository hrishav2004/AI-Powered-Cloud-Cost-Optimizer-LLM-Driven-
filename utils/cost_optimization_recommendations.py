import typer
import json
import pandas as pd

from utils.displays.high_level import high_level
from utils.displays.low_level import low_level

# Produces actionable cost optimization recommendations
def cost_optimization_recommendations():
    # Load the json data from Cost Optimization Report
    with open("cost_optimization_report.json", "r", encoding='utf-8') as f:
        report = f.read()
    report = json.loads(report)

    # Produce a pandas dataframe from the recommendations
    recommendations = report["recommendations"]
    recom_arr = []
    for recom in recommendations:
        row = [recom["title"], recom["service"], recom["current_cost"], recom["potential_savings"], recom["recommendation_type"],
            recom["description"], recom["implementation_effort"], recom["risk_level"], recom["steps"], recom["cloud_providers"]]
        recom_arr.append(row)
    columns = ["Title", "Service", "Current Cost", "Potential Savings", "Recommendation Type", "Description", "Implementation Effort", "Risk Level", "Steps", "Cloud Providers"]
    df = pd.DataFrame(recom_arr, columns=columns)

    # Sort the dataframe by "Potential Savings" in decreasing order
    df.sort_values(by="Potential Savings", ascending=False, inplace=True)
    df.reset_index(inplace=True)

    high_level(df) # Gives a high level overview of the recommendations
    print("\n\n")
    low_level(df)  # Gives a low level deep dive into the details of each recommendation