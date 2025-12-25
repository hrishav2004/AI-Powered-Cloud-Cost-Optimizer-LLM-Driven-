import json, jsonschema
from jsonschema import validate
from utils.LLMCalls.llm_client import llm_client

def generate_cost_optimization_report():
    # Read the prompt for LLM call
    with open("utils/prompts/cost_optimization_report_prompt.txt", "r", encoding='utf-8') as f:
        prompt = f.read()

    # Read the project profile
    with open("pipeline_output/project_profile.json", "r", encoding='utf-8') as f:
        project_profile = f.read()

    # Read the mock billing report
    with open("pipeline_output/mock_billing.json", "r", encoding='utf-8') as f:
        mock_billing = f.read()

    # Read schema for cost optimization report
    with open("utils/schemas/cost_optimization_report_schema.json", "r", encoding='utf-8') as f:
        report_schema = json.load(f)

    cost_optimization_report = llm_client(prompt+" Project profile: "+project_profile+" Mock billing: "+mock_billing, 1500)
    # Validate schema
    validate(instance=json.loads(cost_optimization_report), schema=report_schema)

    # Write the output of LLM to cost_optimization_report.json
    with open("pipeline_output/cost_optimization_report.json", "w", encoding='utf-8') as f:
        f.write(cost_optimization_report)

    # Validate numeric data
    cost_optimization_report = json.loads(cost_optimization_report)
    mock_billing = json.loads(mock_billing)
    cost_optimization_report["analysis"]["total_monthly_cost"] = mock_billing["billing_summary"]["total_cost_inr"]
    cost_optimization_report["analysis"]["budget"] = mock_billing["billing_summary"]["budget_inr"]
    cost_optimization_report["analysis"]["budget_variance"] = cost_optimization_report["analysis"]["budget"] - cost_optimization_report["analysis"]["total_monthly_cost"]
    cost_optimization_report["analysis"]["is_over_budget"] = False
    if cost_optimization_report["analysis"]["total_monthly_cost"]>cost_optimization_report["analysis"]["budget"]:
        cost_optimization_report["analysis"]["is_over_budget"] = True
    savings = [r["potential_savings"] for r in cost_optimization_report["recommendations"]]
    cost_optimization_report["summary"]["total_potential_savings"] = sum(savings)
    cost_optimization_report["summary"]["recommendations_count"] = len(cost_optimization_report["recommendations"])

    with open("pipeline_output/cost_optimization_report.json", "w") as f:
        json.dump(cost_optimization_report, f, indent=4)