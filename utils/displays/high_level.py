import pandas as pd
from rich import print
from rich.prompt import Prompt

def high_level(df: pd.DataFrame):
    total_savings = df["Potential Savings"].sum()
    # Display short summary of all recommendations
    print(f"TOP THREE RECOMMENDATIONS(BASED ON SAVINGS)")
    for idx in range(0, len(df)):
        if(idx==3):
            print(f"OTHER RECOMMENDATIONS")
        curr = df.loc[idx]
        service, title, savings, effort, risk = curr["Service"], curr["Title"], curr["Potential Savings"], curr["Implementation Effort"], curr["Risk Level"]
        percentage_savings = round(savings/total_savings * 100, 1)
        # Color coding: Red for high, Yellow for medium, Green for low
        color1, color2 = "white", "white"   # color1 for effort, color2 for risk
        if effort.lower()=="high":
            color1="red"
        elif effort.lower()=="medium":
            color1="yellow"
        elif effort.lower():
            color1="green"

        if risk.lower()=="high":
            color2="red"
        elif risk.lower()=="medium":
            color2="yellow"
        elif risk.lower():
            color2="green"
        print(f"{idx+1}. [bold underline]For {service}[/bold underline]: {title}. Save [green]\u20B9{savings}[/green] ([white]{percentage_savings}[/white]%) - Effort: [{color1} bold]{effort}[/{color1} bold] - Risk: [{color2} bold]{risk}[/{color2} bold]")