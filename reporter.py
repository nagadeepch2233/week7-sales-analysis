import pandas as pd
import os

REPORTS_DIR = "data/reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

def generate_reports(total_sales, avg_order_value,
                     top_products, monthly_sales, customer_ltv):

    summary_df = pd.DataFrame({
        "Metric": ["Total Sales", "Average Order Value"],
        "Value": [total_sales, avg_order_value]
    })

    summary_df.to_csv(os.path.join(REPORTS_DIR, "summary_report.csv"), index=False)

    with pd.ExcelWriter(os.path.join(REPORTS_DIR, "full_analysis.xlsx")) as writer:
        top_products.to_excel(writer, sheet_name="Top Products")
        monthly_sales.to_excel(writer, sheet_name="Monthly Sales")
        customer_ltv.to_excel(writer, sheet_name="Customer LTV")

    print("Reports generated successfully.\n")
