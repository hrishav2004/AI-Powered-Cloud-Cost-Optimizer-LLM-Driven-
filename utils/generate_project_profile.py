import os
import requests

def generate_project_profile():
    # API_URL = "https://router.huggingface.co/v1/chat/completions"
    # headers = {
    #     "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    # }

    # def query(payload):
    #     response = requests.post(API_URL, headers=headers, json=payload)
    #     return response.json()

    # response = query({
    #     "messages": [
    #         {
    #             "role": "user",
    #             "content": "What is the capital of France?"
    #         }
    #     ],
    #     "model": "meta-llama/Llama-3.1-8B-Instruct:novita"
    # })

    # print(response["choices"][0]["message"])
    print("Reading project description...")
    s=str()
    with open("project_description.txt", "r") as f:
        s=f.read()

    print(s)