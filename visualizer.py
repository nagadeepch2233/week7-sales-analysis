import matplotlib.pyplot as plt
import seaborn as sns
import os

VISUALS_DIR = "data/reports/visuals"
os.makedirs(VISUALS_DIR, exist_ok=True)

def create_visualizations(monthly_sales, category_sales):

    sns.set(style="whitegrid")

    plt.figure(figsize=(10, 6))
    monthly_sales.plot()
    plt.title("Monthly Sales Trend")
    plt.tight_layout()
    plt.savefig(os.path.join(VISUALS_DIR, "monthly_sales_trend.png"))
    plt.close()

    plt.figure(figsize=(8, 8))
    category_sales.plot.pie(autopct="%1.1f%%")
    plt.title("Sales by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(os.path.join(VISUALS_DIR, "category_sales_pie.png"))
    plt.close()

    plt.figure(figsize=(10, 6))
    monthly_sales.plot(kind="bar")
    plt.title("Monthly Sales")
    plt.tight_layout()
    plt.savefig(os.path.join(VISUALS_DIR, "monthly_sales_bar.png"))
    plt.close()

    print("Visualizations saved successfully.\n")
