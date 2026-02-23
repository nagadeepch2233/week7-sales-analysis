import pandas as pd
import pytest
from sales_analyzer.data_cleaner import clean_data

def sample_df():
    return pd.DataFrame({
        "OrderID": [1001, 1002],
        "OrderDate": ["2025-01-01", "2025-01-03"],
        "CustomerID": ["C001", None],
        "Product": ["Laptop", "Mouse"],
        "Category": ["Electronics", "Electronics"],
        "Quantity": ["1", "2"],
        "Price": ["42000", "250"],
        "Region": ["North", "West"]
    })

def test_clean_data_basic():
    df = sample_df()
    clean_df = clean_data(df)
    
    assert clean_df["CustomerID"].isnull().sum() == 0
    
    assert pd.api.types.is_numeric_dtype(clean_df["Quantity"])
    assert pd.api.types.is_numeric_dtype(clean_df["Price"])
    
    assert "TotalSales" in clean_df.columns
    assert clean_df["TotalSales"].iloc[0] == 42000
    assert clean_df["TotalSales"].iloc[1] == 500
