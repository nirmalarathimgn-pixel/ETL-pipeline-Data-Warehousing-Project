# ==========================================
# AUTOMATED ETL & DATA WAREHOUSE PROJECT
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# EXTRACT
# ==========================================

df = pd.read_excel("/content/raw_sales_data.csv.xls")

print("="*50)
print("DATA EXTRACTION COMPLETED")
print("="*50)

print("Rows :", df.shape[0])
print("Columns :", df.shape[1])

# ==========================================
# TRANSFORM
# ==========================================

print("\nRemoving Duplicates...")
df.drop_duplicates(inplace=True)

print("Handling Missing Values...")
df.fillna(0, inplace=True)

print("Converting Date Column...")
df["Order Date"] = pd.to_datetime(df["Order Date"])

print("\nTransformation Completed")

# ==========================================
# LOAD
# ==========================================

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned Data Saved Successfully")

# ==========================================
# KPI ANALYSIS
# ==========================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

print("\nKPI SUMMARY")
print("="*50)

print("Total Sales :", round(total_sales,2))
print("Total Profit :", round(total_profit,2))
print("Total Orders :", total_orders)

# ==========================================
# SALES BY REGION
# ==========================================

sales_region = df.groupby("Region")["Sales"].sum()

print("\nSales By Region")
print(sales_region)

# ==========================================
# SALES BY CATEGORY
# ==========================================

sales_category = df.groupby("Category")["Sales"].sum()

print("\nSales By Category")
print(sales_category)

# ==========================================
# TOP 10 PRODUCTS
# ==========================================

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products")
print(top_products)

# ==========================================
# VISUALIZATION 1
# ==========================================

sales_region.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ==========================================
# VISUALIZATION 2
# ==========================================

sales_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ==========================================
# VISUALIZATION 3
# ==========================================

top_products.plot(kind="bar")

plt.title("Top 10 Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ==========================================
# FINAL MESSAGE
# ==========================================

print("\nETL PIPELINE EXECUTED SUCCESSFULLY")
print("DATA WAREHOUSE READY FOR POWER BI")
