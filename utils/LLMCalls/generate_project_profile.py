import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_project_profile():
    # Read the prompt for LLM call
    # Since the point where this function was called traces back to cost_optimizer.py, the file paths are written w.r.t. the root direcory
    # This path will show error if we directly run generate_project_profile.py
    with open("utils/prompts/project_profile_prompt.txt", "r", encoding='utf-8') as f:
        prompt = f.read()

    # Read the project description
    with open("project_description.txt", "r", encoding='utf-8') as f:
        description = f.read()

    try:
        API_URL = "https://router.huggingface.co/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
        }

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        response = query({
            "messages": [
                {
                    "role": "user",
                    "content": prompt+description
                }
            ],
            "model": "meta-llama/Llama-3.1-8B-Instruct:novita",
            "parameters": {
                "temperature": 0.0,
                "max_tokens": 512
             }
        })

        project_profile = response["choices"][0]["message"]["content"]

        # validate json - to be done later

        # Write the output of LLM to project_profile.json
        with open("project_profile.json", "w", encoding='utf-8') as f:
            f.write(project_profile)

    except Exception as e:
        print(e)