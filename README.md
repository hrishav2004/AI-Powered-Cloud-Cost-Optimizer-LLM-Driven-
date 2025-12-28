<h1>Cloud Cost Optimizer</h1>
<b>Source Code</b>: https://github.com/hrishav2004/AI-Powered-Cloud-Cost-Optimizer-LLM-Driven-<br><br>
<b>Video demonstration</b>: https://drive.google.com/file/d/12H6AdMy8OolQwMsa0_bv6C2GMas9uob_/view?usp=drive_link
<hr>
<p>The Could Cost Optimizer is an AI-powered, CLI based tool that takes user input of a project description and based on the description, generates recommendations for optimization of cost.</p><br>
<p>Following gives the workflow of the Cost Optimizer:</p>
    1. Extracts a structured project profile in JSON format from plain English description provided by the user.<br>
    2. Generates budget-aware synthetic cloud billing based on the project profile.<br>
    3. Analyzes project profile and cloud billing to give recommendations.<br>
    4. Produces strict JSON cost-optimization recommendations.<br>
    5. Exports a pdf report containing the summary, detailed recommendation and service vs cost graph.<br>
    <br>
    <h2>Quick Facts</h2>
    <ul>
        <li>Language: Python</li>
        <li>CLI driven</li>
        <li>LLM backend: Hugging Face Inference API</li>
        <li>Output files stored in pipeline_output folder in the root directory</li>
        <li>Key artifacts per run: project_description.txt, project_profile.json, mock_billing.json, cost_optimization_report.json</li>
    </ul>
<h2>Setup Instructions</h2>

- Clone the repo and enter into the folder.

```bash
git clone https://github.com/hrishav2004/AI-Powered-Cloud-Cost-Optimizer-LLM-Driven-
```
- Create and activate a virtual environment.

```bash
