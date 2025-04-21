import pandas as pd
from sqlalchemy import create_engine

# 1. Connect to SQLite
engine = create_engine("sqlite:///sales.db")

# 2. Load products.csv into the products table
df_prod = pd.read_csv("products.csv")
df_prod.to_sql("products", engine, if_exists="append", index=False)

# 3. Load and transform sales_raw.csv
df_sales = pd.read_csv("sales_raw.csv", parse_dates=["sale_date"])
df_sales["total_amount"] = df_sales["quantity"] * df_sales["unit_price"]

# 4. Append into the sales table
df_sales[["product_id", "sale_date", "quantity", "total_amount"]] \
    .to_sql("sales", engine, if_exists="append", index=False)

print("Data loaded successfully!")
