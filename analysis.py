import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# 1. Connect to SQLite and load the joined table
engine = create_engine("sqlite:///sales.db")
query = """
    SELECT
      s.sale_date,
      p.category,
      s.quantity,
      s.total_amount
    FROM sales s
    JOIN products p
      ON s.product_id = p.product_id
"""
df = pd.read_sql(query, engine, parse_dates=["sale_date"])

# 2. Monthly revenue (sum of total_amount per month)
monthly = (
    df
    .groupby(pd.Grouper(key="sale_date", freq="M"))["total_amount"]
    .sum()
    .reset_index(name="revenue")
)
print("Monthly Revenue:")
print(monthly, "\n")

# 3. Category breakdown
cat_summary = (
    df
    .groupby("category")["total_amount"]
    .agg(total="sum", average="mean", std_dev=lambda x: np.std(x))
    .reset_index()
)
print("Category Summary:")
print(cat_summary, "\n")

# 4. Outlier detection (daily totals > mean + 2·std)
daily = df.groupby("sale_date")["total_amount"].sum()
mu, sigma = daily.mean(), daily.std()
outliers = daily[daily > mu + 2 * sigma].reset_index(name="anomaly_amount")
print("Daily Anomalies:")
print(outliers, "\n")

# 5. Export reports
monthly.to_csv("reports/monthly_revenue.csv", index=False)
cat_summary.to_csv("reports/category_summary.csv", index=False)
outliers.to_csv("reports/daily_anomalies.csv", index=False)
print("✅ Reports written to the ./reports folder")
