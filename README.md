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
        <li>JSON Schema validation</li>
        <li>LLM backend: Hugging Face Inference API</li>
        <li>Output files stored in pipeline_output folder in the root directory</li>
        <li>Key artifacts per run: project_description.txt, project_profile.json, mock_billing.json, cost_optimization_report.json</li>
    </ul>

<h2>Notes on Prompts and LLM Behaviour</h2>

- All prompts live in utils/prompts/ and are deterministic by default (temperature=0.0) to reduce hallucination.
- The max_tokens variable in each LLM call is adjusted according to the size of the prompt and expected size of the response.
- The LLM proposes recommendations — human review required. The system enforces numeric consistency, it does not auto-validate business correctness of steps.
- If a prompt output fails the schema validation, it would ask the user to rerun the cost analysis or enter a more detailed description.

<h2>Setup Instructions</h2>

- Clone the repo and enter into the folder.

```bash
git clone https://github.com/hrishav2004/AI-Powered-Cloud-Cost-Optimizer-LLM-Driven-
```
- Create and activate a virtual environment.

```bash
.\env\Scripts\activate.ps1
```
- Run the root program.

```python
python cost_optimizer.py
```
<h2>Run Steps</h2>

- <b>Enter a new project description</b>: User enters project description in the CLI and the description is written into project_description.txt file.
- <b>Run Complete Cost Analysis</b>: It runs a pipeline of LLM calls as follows:
    - project_description.txt -> project_profile.json
    - project_profile.json -> mock_billing.json
    - project_profile.json + mock_billing.json -> cost_optimization_report.json
- <b>View Recommendations</b>: It shows both the high level and detailed view of the Cost Optimization Recommendations on the CLI. Enter a number between 1 and the no. of recommendations, the details of the corresponding recommendation would display on the terminal.
- <b>Export Report</b>: This would generate a pdf copy of the cost optimization recommendations in the form of a report, named "Cost Optimization Report.pdf".
- <b>Exit</b>: This would exit the program.
<h2>Example Input and Output</h2>
<p>The following contains an example of each of the artifacts:</p>

- project_description.txt
```txt
Hi, I want to build an AI-powered platform that provides a community for people enthusiastic about Machine Learning.  Users can create accounts, connect and chat with co-learners. We are using Angular for frontend, Node.js for backend, MongoDB for database, Nginx as proxy server, Azure for hosting and Hugging Face Inference API for AI support. Monthly budget is up to ₹ 40,000, and we are expecting to support ~20,000 users.
```
- project_profile.json
```json
{
  "name": "AI-powered Community Platform",
  "budget_inr_per_month": 40000,
  "description": "An AI-powered community platform providing a space for Machine Learning enthusiasts to connect, chat, and learn together.",
  "tech_stack": {
    "frontend": "Angular",
    "backend": "Node.js",
    "database": "MongoDB",
    "storage": null,
    "proxy": "Nginx",
    "hosting": "Azure",
    "api": "Hugging Face Inference API",
    "monitoring": null,
    "analytics": null
  },
  "non_functional_requirements": [
    "Scalability",
    "Cost efficiency",
    "Performance"
  ]
}
```
- mock_billing.json
```json
{
    "billing_records": [
        {
            "month": "2025-01",
            "service": "Compute",
            "resource_id": "ai-community-web-01",
            "region": "ap-south-1",
            "usage_type": "Linux/UNIX(on-demand)",
            "usage_quantity": 720,
            "unit": "hours",
            "cost_inr": 840,
            "desc": "Frontend web server"
        },
        {
            "month": "2025-01",
            "service": "Database",
            "resource_id": "ai-community-db-01",
            "region": "ap-south-1",
            "usage_type": "Storage",
            "usage_quantity": 100,
            "unit": "GB-month",
            "cost_inr": 600,
            "desc": "Database storage"
        },
        {
            "month": "2025-01",
            "service": "Storage",
            "resource_id": "ai-community-storage-01",
            "region": "ap-south-1",
            "usage_type": "Storage",
            "usage_quantity": 50,
            "unit": "GB-month",
            "cost_inr": 300,
            "desc": "Media storage"
        },
        {
            "month": "2025-01",
            "service": "Networking",
            "resource_id": "ai-community-network-01",
            "region": "ap-south-1",
            "usage_type": "GB-egress",
            "usage_quantity": 2000,
            "unit": "GB",
            "cost_inr": 1200,
            "desc": "Network egress"
        },
        {
            "month": "2025-01",
            "service": "Monitoring",
            "resource_id": "ai-community-monitoring-01",
            "region": "ap-south-1",
            "usage_type": "Metric data",
            "usage_quantity": 10000,
            "unit": "count",
            "cost_inr": 500,
            "desc": "Monitoring metrics"
        },
        {
            "month": "2025-01",
            "service": "Cache",
            "resource_id": "ai-community-cache-01",
            "region": "ap-south-1",
            "usage_type": "Read requests",
            "usage_quantity": 50000,
            "unit": "count",
            "cost_inr": 250,
            "desc": "Cache read requests"
        },
        {
            "month": "2025-01",
            "service": "LoadBalancer",
            "resource_id": "ai-community-loadbalancer-01",
            "region": "ap-south-1",
            "usage_type": "requests",
            "usage_quantity": 10000,
            "unit": "requests",
            "cost_inr": 1000,
            "desc": "Load balancer requests"
        },
        {
            "month": "2025-01",
            "service": "Backup",
            "resource_id": "ai-community-backup-01",
            "region": "ap-south-1",
            "usage_type": "Storage",
            "usage_quantity": 20,
            "unit": "GB-month",
            "cost_inr": 120,
            "desc": "Backup storage"
        },
        {
            "month": "2025-01",
            "service": "Logging",
            "resource_id": "ai-community-logging-01",
            "region": "ap-south-1",
            "usage_type": "GB-egress",
            "usage_quantity": 100,
            "unit": "GB",
            "cost_inr": 40,
            "desc": "Logging egress"
        },
        {
            "month": "2025-01",
            "service": "Worker",
            "resource_id": "ai-community-worker-01",
            "region": "ap-south-1",
            "usage_type": "Hours",
            "usage_quantity": 300,
            "unit": "hours",
            "cost_inr": 210,
            "desc": "Worker node hours"
        },
        {
            "month": "2025-01",
            "service": "Compute",
            "resource_id": "ai-community-web-02",
            "region": "ap-south-1",
            "usage_type": "Linux/UNIX(on-demand)",
            "usage_quantity": 600,
            "unit": "hours",
            "cost_inr": 420,
            "desc": "Backend web server"
        },
        {
            "month": "2025-01",
            "service": "Database",
            "resource_id": "ai-community-db-02",
            "region": "ap-south-1",
            "usage_type": "Storage",
            "usage_quantity": 80,
            "unit": "GB-month",
            "cost_inr": 480,
            "desc": "Database storage"
        },
        {
            "month": "2025-01",
            "service": "Storage",
            "resource_id": "ai-community-storage-02",
            "region": "ap-south-1",
            "usage_type": "Storage",
            "usage_quantity": 60,
            "unit": "GB-month",
            "cost_inr": 360,
            "desc": "Media storage"
        },
        {
            "month": "2025-01",
            "service": "Networking",
            "resource_id": "ai-community-network-02",
            "region": "ap-south-1",
            "usage_type": "GB-egress",
            "usage_quantity": 1500,
            "unit": "GB",
            "cost_inr": 900,
            "desc": "Network egress"
        },
        {
            "month": "2025-01",
            "service": "Monitoring",
            "resource_id": "ai-community-monitoring-02",
            "region": "ap-south-1",
            "usage_type": "Metric data",
            "usage_quantity": 20000,
            "unit": "count",
            "cost_inr": 1000,
            "desc": "Monitoring metrics"
        },
        {
            "month": "2025-01",
            "service": "Cache",
            "resource_id": "ai-community-cache-02",
            "region": "ap-south-1",
            "usage_type": "Read requests",
            "usage_quantity": 75000,
            "unit": "count",
            "cost_inr": 375,
            "desc": "Cache read requests"
        },
        {
            "month": "2025-01",
            "service": "LoadBalancer",
            "resource_id": "ai-community-loadbalancer-02",
            "region": "ap-south-1",
            "usage_type": "requests",
            "usage_quantity": 15000,
            "unit": "requests",
            "cost_inr": 1500,
            "desc": "Load balancer requests"
        },
        {
            "month": "2025-01",
            "service": "Backup",
            "resource_id": "ai-community-backup-02",
            "region": "ap-south-1",
            "usage_type": "Storage",
            "usage_quantity": 30,
            "unit": "GB-month",
            "cost_inr": 180,
            "desc": "Backup storage"
        }
    ],
    "billing_summary": {
        "budget_inr": 40000,
        "total_cost_inr": 10275,
        "percent_of_budget": 101.4,
        "top_3_services_by_cost": [
            "Compute",
            "Database",
            "Networking"
        ]
    }
}
```
- cost_optimization_report.json
```json
{
    "project_name": "AI-powered Community Platform",
    "analysis": {
        "total_monthly_cost": 10275,
        "budget": 40000,
        "budget_variance": 29725,
        "service_costs": {
            "Compute": 6240,
            "Database": 1080,
            "Storage": 660,
            "Networking": 2100,
            "Monitoring": 1500,
            "Cache": 625,
            "LoadBalancer": 2500,
            "Backup": 300,
            "Logging": 40,
            "Worker": 210
        },
        "high_cost_services": {
            "Compute": 6240,
            "Database": 1080,
            "Networking": 2100
        },
        "is_over_budget": false
    },
    "recommendations": [
        {
            "title": "Migrate to Free Tier Database",
            "service": "Database",
            "current_cost": 1080,
            "potential_savings": 720,
            "recommendation_type": "free_tier",
            "description": "Migrate to free tier database to save costs.",
            "implementation_effort": "low",
            "risk_level": "low",
            "steps": [
                "Check if database usage is within free tier limits.",
                "Migrate to free tier database if eligible."
            ],
            "cloud_providers": [
                "Azure",
                "GCP",
                "DigitalOcean",
                "Open-source"
            ]
        },
        {
            "title": "Rightsizing Compute Instances",
            "service": "Compute",
            "current_cost": 6240,
            "potential_savings": 1560,
            "recommendation_type": "rightsizing",
            "description": "Rightsizing compute instances to save costs.",
            "implementation_effort": "medium",
            "risk_level": "medium",
            "steps": [
                "Review compute instance usage and adjust instance types.",
                "Implement auto-scaling to adjust instance counts."
            ],
            "cloud_providers": [
                "AWS",
                "Azure",
                "GCP",
                "DigitalOcean",
                "On-prem"
            ]
        },
        {
            "title": "Storage Tiering",
            "service": "Storage",
            "current_cost": 660,
            "potential_savings": 110,
            "recommendation_type": "storage_tier",
            "description": "Implement storage tiering to save costs.",
            "implementation_effort": "low",
            "risk_level": "low",
            "steps": [
                "Implement storage tiering by moving less frequently used data to lower-cost storage tiers."
            ],
            "cloud_providers": [
                "AWS",
                "Azure",
                "GCP",
                "DigitalOcean",
                "On-prem"
            ]
        },
        {
            "title": "Reserved Instances for Compute",
            "service": "Compute",
            "current_cost": 6240,
            "potential_savings": 624,
            "recommendation_type": "reserved_instances",
            "description": "Purchase reserved instances for compute to save costs.",
            "implementation_effort": "high",
            "risk_level": "high",
            "steps": [
                "Calculate potential savings from reserved instances.",
                "Purchase reserved instances for compute."
            ],
            "cloud_providers": [
                "AWS",
                "Azure",
                "GCP",
                "DigitalOcean",
                "On-prem"
            ]
        },
        {
            "title": "Caching for Database",
            "service": "Cache",
            "current_cost": 625,
            "potential_savings": 125,
            "recommendation_type": "caching",
            "description": "Implement caching for database to save costs.",
            "implementation_effort": "low",
            "risk_level": "low",
            "steps": [
                "Implement caching layer between application and database."
            ],
            "cloud_providers": [
                "AWS",
                "Azure",
                "GCP",
                "DigitalOcean",
                "On-prem"
            ]
        },
        {
            "title": "Load Balancer Optimization",
            "service": "LoadBalancer",
            "current_cost": 2500,
            "potential_savings": 500,
            "recommendation_type": "network_optimization",
            "description": "Optimize load balancer configuration to save costs.",
            "implementation_effort": "medium",
            "risk_level": "medium",
            "steps": [
                "Review load balancer configuration and optimize it.",
                "Implement load balancer auto-scaling."
            ],
            "cloud_providers": [
                "AWS",
                "Azure",
                "GCP",
                "DigitalOcean",
                "On-prem"
            ]
        },
        {
            "title": "Migrate to Azure for Compute",
            "service": "Compute",
            "current_cost": 6240,
            "potential_savings": 624,
            "recommendation_type": "alternative_provider",
            "description": "Migrate to Azure for compute to save costs.",
            "implementation_effort": "high",
            "risk_level": "high",
            "steps": [
                "Calculate potential savings from migration.",
                "Migrate compute to Azure."
            ],
            "cloud_providers": [
                "Azure",
                "GCP",
                "DigitalOcean",
                "On-prem"
            ]
        },
        {
            "title": "Backup Optimization",
            "service": "Backup",
            "current_cost": 300,
            "potential_savings": 60,
            "recommendation_type": "backup_optimization",
            "description": "Optimize backup configuration to save costs.",
            "implementation_effort": "low",
            "risk_level": "low",
            "steps": [
                "Review backup configuration and optimize it.",
                "Implement backup auto-scaling."
            ],
            "cloud_providers": [
                "AWS",
                "Azure",
                "GCP",
                "DigitalOcean",
                "On-prem"
            ]
        },
        {
            "title": "Reserved Instances for Database",
            "service": "Database",
            "current_cost": 1080,
            "potential_savings": 108,
            "recommendation_type": "reserved_instances",
            "description": "Purchase reserved instances for database to save costs.",
            "implementation_effort": "high",
            "risk_level": "high",
            "steps": [
                "Calculate potential savings from reserved instances.",
                "Purchase reserved instances for database."
            ],
            "cloud_providers": [
                "AWS",
                "Azure",
                "GCP",
                "DigitalOcean",
                "On-prem"
            ]
        }
    ],
    "summary": {
        "total_potential_savings": 4431,
        "savings_percentage": 62.1,
        "recommendations_count": 9,
        "high_impact_recommendations": 3
    }
}
```
- Cost Optimization Report.pdf
[Cost Optimization Report.pdf](https://github.com/user-attachments/files/24364897/Cost.Optimization.Report.pdf)
