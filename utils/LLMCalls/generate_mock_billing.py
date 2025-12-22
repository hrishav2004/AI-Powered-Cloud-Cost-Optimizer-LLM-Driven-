from utils.LLMCalls.llm_client import llm_client

def generate_mock_billing():
    # Read the prompt for LLM call
    with open("utils/prompts/mock_billing_prompt.txt", "r", encoding='utf-8') as f:
        prompt = f.read()

    # Read the project profile
    with open("project_profile.json", "r", encoding='utf-8') as f:
        project_profile = f.read()

    try:
        mock_billing = llm_client(prompt+project_profile, 1500)

        # Write the output of LLM to mock_billing.json
        with open("mock_billing.json", "w", encoding='utf-8') as f:
            f.write(mock_billing)
            
    except Exception as e:
        print(e)