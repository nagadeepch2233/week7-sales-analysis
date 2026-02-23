import argparse
from sales_analyzer import (
    load_data,
    clean_data,
    basic_analysis,
    advanced_analysis,
    create_visualizations,
    generate_reports
)

def main():
    parser = argparse.ArgumentParser(description="Sales Data Analysis System")
    parser.add_argument("--file", default="data/raw/sales_data.csv", help="Path to CSV/XLSX file")
    parser.add_argument("--analysis", choices=["basic", "advanced", "full"], default="full")
    args = parser.parse_args()

    # Load & clean data
    df = load_data(args.file)
    df = clean_data(df)

    if args.analysis in ["basic", "full"]:
        total_sales, avg_order_value, top_products, category_sales = basic_analysis(df)

    if args.analysis in ["advanced", "full"]:
        monthly_sales, monthly_growth, customer_ltv, forecast = advanced_analysis(df)

    if args.analysis == "full":
        create_visualizations(monthly_sales, category_sales)
        generate_reports(total_sales, avg_order_value, top_products, monthly_sales, customer_ltv)

if __name__ == "__main__":
    main()
