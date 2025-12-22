# This file is the wrapper for HuggingFace Inference API
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def llm_client(full_prompt, max_tokens=512):
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
                "content": full_prompt
            }
        ],
        "model": "meta-llama/Llama-3.1-8B-Instruct:novita",
        "parameters": {
            "temperature": 0.0,
            "max_tokens": max_tokens
            }
    })

    return response["choices"][0]["message"]["content"]