# End-to-End-Vendor-Analysis-for-Profitability-Optimization
This project addresses a critical business challenge in the retail and wholesale industry: optimizing profitability through effective inventory and sales management. The analysis aims to prevent losses that arise from inefficient pricing strategies, poor inventory turnover, and excessive vendor dependency.

## 📖 Table of Contents
* Project Overview

* Business Problem & Objectives

* 🛠️ Tech Stack

* ⚙️ Project Workflow

* 📊 Key Findings & Insights

* 📂 Repository Structure

* 🚀 How to Run This Project

* 📞 Contact

## 🌐 Project Overview
This repository contains a comprehensive, end-to-end data analytics project that mirrors a real-world business scenario in the retail and wholesale industry. The project starts with raw, multi-source transactional data and progresses through ETL, data warehousing, in-depth analysis, statistical validation, and finally, the creation of an interactive business intelligence dashboard. The primary goal is to analyze vendor and brand performance to uncover actionable insights that drive profitability and operational efficiency.

## 🎯 Business Problem & Objectives
A retail/wholesale company is facing challenges with profitability due to inefficient pricing, poor inventory turnover, and over-reliance on a few key vendors. This analysis was commissioned to address these issues.

The primary objectives are:

+ Identify Underperforming Brands: Find brands with low sales but high profit margins that are candidates for promotional and pricing adjustments.

+ Pinpoint Top Vendors: Determine which vendors contribute most significantly to sales and gross profit.

+ Analyze Bulk Purchasing Impact: Assess how purchasing in bulk affects unit costs to optimize procurement strategies.

+ Evaluate Inventory Turnover: Identify vendors with slow-moving products to reduce holding costs and improve stock efficiency.

+ Investigate Profitability Variance: Statistically compare the profit margins of high-performing vs. low-performing vendors.

##  🛠️ Tech Stack
Data Ingestion & Transformation (ETL): Python (Pandas, SQLAlchemy)

Database: SQLite

Data Analysis & Statistics: Python (NumPy, SciPy, Statsmodels), Jupyter Notebook

Data Visualization: Matplotlib, Seaborn, Power BI

Business Intelligence & Dashboarding: Power BI, DAX

## ⚙️ Project Workflow
The project was executed in three distinct phases, creating a robust and reproducible pipeline from raw data to final insights.

### Phase 1: ETL & Data Warehousing

Ingestion: Developed a scalable Python script (ingestion_db.py) to ingest multiple large CSVs into a central SQLite database. The script includes robust logging for monitoring and error tracking.

Aggregation & Optimization: Created a second script (get_vendor_summary.py) to execute a complex, optimized SQL query. This query joins and pre-aggregates data from multiple tables, transforming over 20 million transactional records into a clean, analysis-ready summary table of ~10,000 records. This step was critical for performance and analytical efficiency.

### Phase 2: Exploratory Data Analysis (EDA) & Statistical Validation

Data Exploration: Used a Jupyter Notebook (Exploratory Data Analysis.ipynb) to perform initial exploration directly on the database tables using SQL to understand relationships and data quality.

In-depth Analysis: In a second notebook (Vendor Performance Analysis.ipynb), conducted a deep-dive analysis on the final aggregated table. This included:

Feature Engineering: Created new metrics like Gross Profit, Profit Margin, and Stock Turnover Ratio.

Visualization: Generated plots to identify trends, outliers, and correlations.

Hypothesis Testing: Used a T-test to statistically validate the difference in profit margins between vendor groups.

### Phase 3: Dashboarding & Reporting

Interactive Dashboard: Developed a dynamic Power BI dashboard (Vendor Performance Power BI Dashboard.pbix) to present findings. The dashboard includes KPIs, interactive charts, and drill-down capabilities for stakeholder exploration.

Final Report: Compiled a detailed PDF report (Project Report.pdf) summarizing the methodology, key findings, and strategic business recommendations.

## 📊 Key Findings & Insights
This analysis uncovered several critical, data-driven insights:

💰 Unsold Capital: Identified $2.7 million in capital locked in unsold inventory, highlighting a major opportunity for inventory optimization.

🎯 Promotional Strategy: Pinpointed 198 brands with low sales but high profit margins, making them prime candidates for targeted promotional campaigns to boost sales volume.

🔗 Vendor Dependency: Revealed that the top 10 vendors account for over 65% of total purchase dollars, indicating a high supply chain dependency risk.

📦 Bulk Purchasing Impact: Confirmed that bulk purchasing is highly effective, with large orders achieving up to a 72% reduction in unit cost compared to small orders.

## 📂 Repository Structure

├── 📄 README.md
├── data/
│   ├── begin_inventory.csv
│   ├── end_inventory.csv
│   ├── purchases.csv
│   ├── purchase_prices.csv
│   ├── sales.csv
│   └── vendor_invoice.csv
├── scripts/
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
├── notebooks/
│   ├── Exploratory Data Analysis.ipynb
│   └── Vendor Performance Analysis.ipynb
├── dashboard/
│   ├── Vendor Performance Power BI Dashboard.pbix
│   └── Vendor Performance Power BI Dashboard.pdf
└── report/
    └── Project Report.pdf


data/: Contains sample CSV files (100 rows each) representing the raw data sources.

scripts/: Contains the Python scripts for the ETL pipeline.

notebooks/: Contains the Jupyter Notebooks used for data exploration and analysis.

dashboard/: Contains the final Power BI dashboard file and a PDF export for easy viewing.

report/: Contains the final, detailed project report.

## 🚀 How to Run This Project
Follow these steps to replicate the analysis on your local machine.

Prerequisites
Python 3.8+

Jupyter Notebook or JupyterLab

Required Python libraries: pandas, sqlalchemy, numpy, matplotlib, seaborn, scipy, statsmodels. You can install them via pip:

pip install pandas sqlalchemy numpy matplotlib seaborn scipy statsmodels notebook

Microsoft Power BI Desktop (for interacting with the .pbix file).

Steps
Clone the repository:

git clone https://github.com/nipunchauhan/End-to-End-Vendor-Analysis-for-Profitability-Optimization.git <br> cd End-to-End-Vendor-Analysis-for-Profitability-Optimization

Run the ETL Pipeline:
Execute the Python scripts from your terminal in the following order to create and populate the SQLite database (inventory.db).

### Step 1: Ingest raw data into the database
python scripts/ingestion_db.py

### Step 2: Create the final aggregated summary table
python scripts/get_vendor_summary.py

Explore the Analysis:
Launch Jupyter Notebook to explore the analysis process.

jupyter notebook

Navigate to the notebooks/ directory and open EDA_SQL.ipynb and Vendor_Performance_Analysis.ipynb. You can run the cells to see the step-by-step analysis.

View the Dashboard:

Open the dashboard/Vendor_Performance_Dashboard.pbix file in Power BI Desktop to interact with the full dashboard.

Alternatively, view the dashboard/Vendor_Performance_Dashboard.pdf for a static version.

## 📞 Contact

Nipun Chauhan
Email: nipunct@gmail.com
