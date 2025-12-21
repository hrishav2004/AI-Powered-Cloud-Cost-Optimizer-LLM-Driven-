import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_project_profile():

    description=str()
    with open("project_description.txt", "r", encoding='utf-8') as f:
        description=f.read()

    # print("Generating project profile...")

    prompt_to_generate_project_profile = os.environ["PROMPT_1"] + description
    # print(prompt_to_generate_project_profile)

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
                    "content": prompt_to_generate_project_profile
                }
            ],
            "model": "meta-llama/Llama-3.1-8B-Instruct:novita",
            "parameters": {
                "temperature": 0.0,
                "max_tokens": 512
             }
        })

        print(response["choices"][0]["message"]["content"])
    except Exception as e:
        print(e)
    
    print("Reading project description...")