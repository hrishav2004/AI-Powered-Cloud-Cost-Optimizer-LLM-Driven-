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

    try:
        cost_optimization_report = llm_client(prompt+" Project profile: "+project_profile+" Mock billing: "+mock_billing, 1500)

        # Write the output of LLM to cost_optimization_report.json
        with open("pipeline_output/cost_optimization_report.json", "w", encoding='utf-8') as f:
            f.write(cost_optimization_report)

    except Exception as e:
        print(e)