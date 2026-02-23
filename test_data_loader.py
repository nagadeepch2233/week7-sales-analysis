import pytest
import os
import pandas as pd
from sales_analyzer.data_loader import load_data

TEST_FILE = os.path.join("data", "raw", "sales_data.csv")

def test_load_csv_file():
    df = load_data(TEST_FILE)
    assert isinstance(df, pd.DataFrame), "Output should be a pandas DataFrame"
    assert not df.empty, "DataFrame should not be empty"
    required_cols = ["OrderID", "OrderDate", "CustomerID", "Product", "Category", "Quantity", "Price", "Region"]
    for col in required_cols:
        assert col in df.columns, f"Missing column: {col}"

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_data("non_existent_file.csv")

def test_unsupported_format(tmp_path):
    tmp_file = tmp_path / "data.txt"
    tmp_file.write_text("test")
    with pytest.raises(ValueError):
        load_data(str(tmp_file))
