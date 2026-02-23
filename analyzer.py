def basic_analysis(df):

    print("===== BASIC ANALYSIS =====")

    total_sales = df["TotalSales"].sum()
    avg_order_value = df["TotalSales"].mean()

    top_products = (
        df.groupby("Product")["TotalSales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    category_sales = (
        df.groupby("Category")["TotalSales"]
        .sum()
        .sort_values(ascending=False)
    )

    print(f"Total Sales: ₹{total_sales:,.2f}")
    print(f"Average Order Value: ₹{avg_order_value:,.2f}")
    print("\nTop 5 Products:\n", top_products)

    return total_sales, avg_order_value, top_products, category_sales

def advanced_analysis(df):

    print("\n===== ADVANCED ANALYSIS =====")

    df["Month"] = df["OrderDate"].dt.to_period("M")

    monthly_sales = df.groupby("Month")["TotalSales"].sum()
    monthly_growth = monthly_sales.pct_change() * 100

    customer_ltv = (
        df.groupby("CustomerID")["TotalSales"]
        .sum()
        .sort_values(ascending=False)
    )

    forecast = monthly_sales.rolling(window=3).mean()

    print("Advanced analysis completed.\n")

    return monthly_sales, monthly_growth, customer_ltv, forecast
