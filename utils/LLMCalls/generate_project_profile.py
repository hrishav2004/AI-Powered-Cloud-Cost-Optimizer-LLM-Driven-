import json, jsonschema
from jsonschema import validate
from utils.LLMCalls.llm_client import llm_client

def generate_project_profile():
    # Read the prompt for LLM call
    # Since the point where this function was called traces back to cost_optimizer.py, the file paths are written w.r.t. the root direcory
    # This path will show error if we directly run generate_project_profile.py
    with open("utils/prompts/project_profile_prompt.txt", "r", encoding='utf-8') as f:
        prompt = f.read()

    # Read the project description
    with open("pipeline_output/project_description.txt", "r", encoding='utf-8') as f:
        description = f.read()

    # Read schema for project profile
    with open("utils/schemas/project_profile_schema.json", "r", encoding='utf-8') as f:
        profile_schema = json.load(f)

    project_profile = llm_client(prompt+description)
    # Validate schema
    validate(instance=json.loads(project_profile), schema=profile_schema)


    # Write the output of LLM to project_profile.json
    with open("pipeline_output/project_profile.json", "w", encoding='utf-8') as f:
        f.write(project_profile)