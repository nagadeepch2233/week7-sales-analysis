import pytest
import os
import pandas as pd
from sales_analyzer.data_loader import load_data

TEST_FILE = os.path.join("data", "raw", "sales_data.csv")

def test_load_csv_file():
    df = load_data(TEST_FILE)
    
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 10  # 10 rows in sample data
    required_cols = ["OrderID", "OrderDate", "CustomerID", "Product", "Category", "Quantity", "Price", "Region"]
    for col in required_cols:
        assert col in df.columns

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_data("non_existent_file.csv")

def test_unsupported_format(tmp_path):
    tmp_file = tmp_path / "data.txt"
    tmp_file.write_text("sample")
    with pytest.raises(ValueError):
        load_data(str(tmp_file))))
