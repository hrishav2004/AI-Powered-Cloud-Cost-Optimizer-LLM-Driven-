import json, os, pandas as pd, numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
from rich import print

# Exports report as a pdf
def export_reports():
    print("Exporting report...")

    with open("cost_optimization_report.json", "r", encoding='utf-8') as f:
        report = f.read()
    report = json.loads(report)
    analysis = report["analysis"]
    recommendations = report["recommendations"]
    project_name, cost, budget, variance, service_costs = report["project_name"], analysis["total_monthly_cost"], analysis["budget"], analysis["budget_variance"], analysis["service_costs"]
    over_budget = "No"
    if analysis["is_over_budget"]:
        over_budget = "Yes"
    TABLE_DATA = [["Service", "Cost(in INR)"]]
    for key, value in service_costs.items():
        TABLE_DATA.append([key, str(value)])

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    # Heading
    pdf.add_page()
    pdf.set_font("Times")
    pdf.set_font(style="BU", size=30)
    pdf.set_text_color(0,0,255)
    pdf.cell(0, 20, "Cost Optimization Report", new_x="LMARGIN", new_y="NEXT", align="C")
    # Project Summary
    pdf.set_font(style="BU", size=20)
    pdf.set_text_color(0,0,0)
    pdf.cell(0, 20, "Project Summary", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(size=14)
    pdf.write_html(f"""
        <p><b>Name of the project</b>: {project_name}</p>
        <p><b>Total monthly cost</b>: Rs. {cost}</p>
        <p><b>Budget</b>: Rs. {budget}</p>
        <p><b>Budget variance</b>: Rs. {variance}</p>
        <p><b>Over budget</b>: {over_budget}</p>
        <p><b>Service Cost summary:</b></p>
        <br>
    """)
    with pdf.table(text_align="CENTER", width=150) as table:
        for data_row in TABLE_DATA:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    # Bar graph and pie chart
    pdf.add_page()
    service, costs = [], []
    for key, value in service_costs.items():
        service.append(key)
        costs.append(value)
    costs = np.array(costs)
    plt.figure(figsize=(15,5))
    plt.bar(service, costs)
    plt.title("Service vs Cost breakdown", fontsize=15)
    plt.xlabel("Service", fontsize=12)
    plt.ylabel("Cost(in INR)", fontsize=12)
    plt.savefig("barchart.svg", format="svg")
    pdf.image("barchart.svg", x=10, y=25, w=200, h=120)
    os.remove("barchart.svg")
    plt.close()
    plt.pie(costs, labels=service)
    plt.title("Service Cost Distribution")
    plt.savefig("piechart.svg", format="svg")
    pdf.image("piechart.svg", x=10, y=170, w=200, h=120)
    os.remove("piechart.svg")
    plt.close()

    recom_arr = []
    for recom in recommendations:
        row = [recom["title"], recom["service"], recom["current_cost"], recom["potential_savings"], recom["recommendation_type"],
            recom["description"], recom["implementation_effort"], recom["risk_level"], recom["steps"], recom["cloud_providers"]]
        recom_arr.append(row)
    columns = ["Title", "Service", "Current Cost", "Potential Savings", "Recommendation Type", "Description", "Implementation Effort", "Risk Level", "Steps", "Cloud Providers"]
    df = pd.DataFrame(recom_arr, columns=columns)
    df.sort_values(by="Potential Savings", ascending=False, inplace=True)
    df.reset_index(inplace=True)

    # Summary of recommendations
    pdf.add_page()
    pdf.set_font("Times", style="U", size=25)
    pdf.cell(0, 10, "Summary of Recommendations", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Times", style="", size=15)
    for idx in range(0, len(df)):
        service, title = df.loc[idx]["Service"], df.loc[idx]["Title"]
        pdf.cell(0, 10, f"{idx+1}. {title} ({service})", new_x="LMARGIN", new_y="NEXT")

    # Detailed recommendations
    for idx in range(0, len(df)):
        curr = df.loc[idx]
        service, title, cost, savings, description, effort, risk, steps, cloud_providers = curr["Service"], curr["Title"], curr["Current Cost"], curr["Potential Savings"], curr["Description"], curr["Implementation Effort"], curr["Risk Level"], curr["Steps"], curr["Cloud Providers"]
        providers = ""
        for provider in cloud_providers:
            providers += (provider+", ")
        providers = providers[0:-2]
        pdf.add_page()
        pdf.set_font("Times", style="BU", size=25)
        pdf.cell(0, 20, f"{title}", new_x="LMARGIN", new_y="NEXT", align="C")
        pdf.set_font("Times", style="", size=20)
        pdf.write_html(f"""
            <p>Optimization in terms of <b>{service}</b>.</p>
            <i>{description}</i>
            <p>Original cost is Rs. <b>{cost}</b>, savings upto Rs. <b>{round(savings)}</b>. Almost <b>{round(savings*100/cost)}</b>% cost cutting.</p>
            <p>Implementation effort is <i>{effort}</i>, poses <i>{risk}</i> risk.</p>
            <u>Steps of implementation:</u>
        """)
        for i in range(0, len(steps)):
            pdf.cell(0, 10, f"{i+1}. {steps[i]}", new_x="LMARGIN", new_y="NEXT")
        
        pdf.write_html(f"""
            <p><u>Cloud Providers</u>: {providers}</p>
        """)

    # Bar graph for cost cutting
    pdf.add_page()
    curr_cost = df["Current Cost"]
    pot_savings = df["Potential Savings"]
    proj_cost = curr_cost-pot_savings
    title = df["Title"]
    plt.figure(figsize=(15,5))
    plt.barh(title, curr_cost, label="Current Cost")
    plt.barh(title, proj_cost, label="Projected Cost (After Savings)")
    plt.title("Cost Impact per Recommendation")
    plt.xlabel("Cost", fontsize=15)
    plt.ylabel("Recommendation", fontsize=15)
    plt.legend()
    plt.savefig("barchart2.svg", format="svg")
    pdf.image("barchart2.svg", x=20, y=25, w=190, h=200)
    os.remove("barchart2.svg")
    plt.close()

    # Export report as pdf
    pdf.output("Cost Optimization Report.pdf")
    print("[bold green]Succesfully downloaded report![/bold green]")