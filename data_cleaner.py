import pandas as pd

def clean_data(df):

    required_columns = [
        "OrderID", "OrderDate", "CustomerID",
        "Product", "Category", "Quantity",
        "Price", "Region"
    ]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df = df.drop_duplicates()

    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    df["CustomerID"] = df["CustomerID"].fillna("Unknown")
    df["Quantity"] = df["Quantity"].fillna(0)
    df["Price"] = df["Price"].fillna(0)

    df = df.dropna(subset=["OrderDate"])

    df["TotalSales"] = df["Quantity"] * df["Price"]

    print("Data Cleaned Successfully!\n")
    return df
