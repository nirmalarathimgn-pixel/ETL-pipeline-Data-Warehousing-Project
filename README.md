🚀 ETL Pipeline & Data Warehouse Analytics Project 

📊 End-to-End Data Engineering & Business Intelligence Solution using ETL Processes, Star Schema Data Warehouse Design, Data Modeling, and Power BI Reporting.

📌 Project Overview

This project demonstrates the complete lifecycle of a modern Data Warehouse solution:

✅ Data Extraction from multiple sources

✅ Data Cleaning & Transformation

✅ Data Warehouse Development

✅ Star Schema Data Modeling

✅ Fact & Dimension Table Design

✅ KPI Development using DAX

✅ Interactive Business Intelligence Dashboards

The project enables organizations to transform raw transactional data into meaningful business insights for strategic decision-making.

🎯 Business Objective

The objective of this project is to:

Build a scalable Data Warehouse
Centralize sales and customer data
Improve reporting efficiency
Enable faster business decisions
Provide a single source of truth for analytics

🏗️ Data Warehouse Architecture
Data Sources
     │
     ▼
ETL Pipeline
(Extract → Transform → Load)
     │
     ▼
Data Warehouse
(Star Schema)
     │
     ▼
Power BI Dashboard
     │
     ▼
Business Insights
🔄 ETL Process
1️⃣ Extract

Data collected from:

Sales Data
Customer Data
Product Data
Budget Data
Calendar Data
Extracted Fields
Customer Information
Product Information
Sales Transactions
Budget Data
Date Information
2️⃣ Transform

Performed using Power Query:

Data Cleaning
Removed Null Values
Removed Duplicate Records
Corrected Data Types
Standardized Formats
Created Business Rules
Data Transformation
Generated Surrogate Keys
Created Customer Segments
Built Date Hierarchies
Derived Business Metrics
Aggregated Data
3️⃣ Load

Loaded transformed data into:

Data Warehouse

Fact Tables

FACT_InternetSales
FACT_Budget

Dimension Tables

DIM_Calendar
DIM_Customers
DIM_Products
⭐ Star Schema Design

The Data Warehouse follows a Star Schema architecture.

                DIM_Calendar
                      │
                      │
DIM_Customers ── FACT_InternetSales ── DIM_Products
                      │
                      │
                 FACT_Budget
Benefits

✅ Faster Query Performance

✅ Better Scalability

✅ Optimized Reporting

✅ Simplified Data Relationships

✅ Industry Standard Design

📊 Fact Tables
FACT_InternetSales

Stores transactional sales data.

Columns
CustomerKey
ProductKey
OrderDateKey
DueDateKey
ShipDateKey
SalesAmount
SalesOrderNumber
Purpose
Revenue Analysis
Order Tracking
Product Performance
Customer Analytics
FACT_Budget

Stores business targets and budget information.

Columns
Date
Budget
Purpose
Budget Tracking
Variance Analysis
Performance Monitoring
📋 Dimension Tables
DIM_Customers

Contains customer-related information.

Columns
CustomerKey
FirstName
LastName
FullName
Gender
CustomerCity
DateFirstPurchase
Purpose
Customer Segmentation
Customer Analysis
Geographic Reporting
DIM_Products

Contains product master data.

Columns
ProductKey
ProductName
ProductCategory
ProductSubcategory
ProductModelName
ProductColor
ProductSize
ProductLine
ProductStatus
ProductDescription
ProductItemCode
Purpose
Product Analytics
Category Analysis
Inventory Insights
DIM_Calendar

Contains date-related attributes.

Columns
Date
Year
Quarter
Month
MonthShort
MonthNumber
Week
WeekNumber
Purpose
Time Intelligence
Monthly Analysis
Quarterly Reporting
Trend Analysis
📈 Key KPIs
Total Revenue =
SUM(FACT_InternetSales[SalesAmount])

Total Orders =
DISTINCTCOUNT(
FACT_InternetSales[SalesOrderNumber]
)

Average Selling Price =
DIVIDE(
[Total Revenue],
[Total Orders]
)

Budget Amount =
SUM(FACT_Budget[Budget])

Budget Achievement % =
DIVIDE(
[Total Revenue],
[Budget Amount]
)

Revenue Variance =
[Total Revenue] -
[Budget Amount]
📊 Power BI Dashboards
Sales Overview

📈 Revenue Trends

💰 Budget vs Actual

🏆 Top Products

👥 Top Customers

🌍 City Performance

Customer Analytics

👤 Customer Segmentation

🚻 Gender Analysis

🌍 Geographic Distribution

💵 High-Value Customers

Product Analytics

📦 Category Performance

📊 Subcategory Trends

🏆 Best-Selling Products

📈 Revenue Contribution

Executive Insights

🎯 Budget Achievement

🏆 Top Revenue Category

🌍 Top Revenue City

📅 Best Performing Month

📊 Strategic Business Recommendations

🔍 Business Insights Generated
Revenue Insights
Revenue peaks during December.
February shows the lowest performance.
Revenue trends reveal seasonal demand patterns.
Customer Insights
High-value customers contribute the majority of sales.
Customer concentration drives significant revenue.
Product Insights
Bikes are the highest revenue-generating category.
Road Bikes contribute the largest revenue share.
Regional Insights
London is the highest-performing city.
A few cities generate most of the revenue.
🛠️ Skills Demonstrated
Data Engineering

✔ ETL Development

✔ Data Warehousing

✔ Data Modeling

✔ Star Schema Design

✔ Data Integration

✔ Data Transformation

Power BI

✔ Power Query

✔ DAX

✔ KPI Development

✔ Dashboard Design

✔ Interactive Reporting

✔ Data Visualization

Analytics

✔ Business Intelligence

✔ Revenue Analysis

✔ Customer Analytics

✔ Product Analytics

✔ Budget Analysis

✔ Executive Reporting

🚀 Project Outcome

✅ Built a scalable Data Warehouse

✅ Implemented ETL Pipeline

✅ Designed Star Schema Model

✅ Improved Reporting Efficiency

✅ Enabled Self-Service Analytics

✅ Delivered Actionable Business Insights
