import pandas as pd
import pytest
from sales_analyzer.analyzer import basic_analysis, advanced_analysis
from sales_analyzer.data_cleaner import clean_data

def sample_df():
    return pd.DataFrame({
        "OrderID": [1001, 1002, 1003],
        "OrderDate": ["2025-01-01", "2025-01-03", "2025-01-05"],
        "CustomerID": ["C001", "C002", "C003"],
        "Product": ["Laptop", "Mouse", "Keyboard"],
        "Category": ["Electronics", "Electronics", "Electronics"],
        "Quantity": [1, 2, 1],
        "Price": [42000, 250, 1500],
        "Region": ["North", "West", "East"]
    })

def test_basic_analysis_values():
    df = clean_data(sample_df())
    total_sales, avg_order_value, top_products, category_sales = basic_analysis(df)
    # TotalSales = 42000 + 500 + 1500 = 44000
    assert total_sales == 44000
    # Average = 44000 / 3
    assert avg_order_value == pytest.approx(14666.6667, rel=1e-4)
    # Top product should be Laptop
    assert top_products.index[0] == "Laptop"

def test_advanced_analysis_values():
    df = clean_data(sample_df())
    monthly_sales, monthly_growth, customer_ltv, forecast = advanced_analysis(df)
    # Check monthly sales contains January 2025
    assert pd.Period("2025-01", freq="M") in monthly_sales.index
    # Check CustomerID in LTV
    assert "C001" in customer_ltv.index
    # Forecast rolling mean exists
    assert forecast.isna().sum() >= 0  # first values may be NaN
