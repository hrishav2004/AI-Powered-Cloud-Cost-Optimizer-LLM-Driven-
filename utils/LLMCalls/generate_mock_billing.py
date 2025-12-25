import json, jsonschema
from jsonschema import validate
from utils.LLMCalls.llm_client import llm_client

def generate_mock_billing():
    # Read the prompt for LLM call
    with open("utils/prompts/mock_billing_prompt.txt", "r", encoding='utf-8') as f:
        prompt = f.read()

    # Read the project profile
    with open("pipeline_output/project_profile.json", "r", encoding='utf-8') as f:
        project_profile = f.read()

    # Read schema for mock billing
    with open("utils/schemas/mock_billing_schema.json", "r", encoding='utf-8') as f:
        billing_schema = json.load(f)

    mock_billing = llm_client(prompt+project_profile, 1500)
    # Validate schema
    validate(instance=json.loads(mock_billing), schema=billing_schema)

    # Write the output of LLM to mock_billing.json
    with open("pipeline_output/mock_billing.json", "w", encoding='utf-8') as f:
        f.write(mock_billing)

    # Validate numeric data
    mock_billing = json.loads(mock_billing)
    project_profile = json.loads(project_profile)
    mock_billing["billing_summary"]["budget_inr"] = project_profile["budget_inr_per_month"]
    cost_records = [record["cost_inr"] for record in mock_billing["billing_records"]]
    mock_billing["billing_summary"]["total_cost_inr"] = sum(cost_records)

    with open("pipeline_output/mock_billing.json", "w") as f:
        json.dump(mock_billing, f, indent=4)