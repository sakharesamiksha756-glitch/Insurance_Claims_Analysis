# Insurance Claims Analysis for Risk and Fraud Detection

## Project Overview

This project analyzes insurance claims data to identify patterns associated with fraudulent claims and provide data-driven insights for risk analysis.

The analysis combines Python, SQL, SQLite, and Power BI to clean the data, explore fraud patterns, perform structured analysis, and build an interactive dashboard.

## Objective

- Analyze insurance claim data and identify patterns associated with fraudulent claims.
- Calculate fraud rates across different claim characteristics.
- Use SQL to perform structured fraud analysis.
- Build an interactive Power BI dashboard for visual analysis.
- Generate business insights that can support insurance claim risk monitoring.

## Tools & Technologies

- **Python** — Data inspection, cleaning, exploratory data analysis (EDA), and visualization
- **Pandas** — Data manipulation and analysis
- **Matplotlib** — Data visualization
- **SQLite** — Database storage and querying
- **SQL** — Fraud analysis and aggregation
- **Power BI** — Interactive dashboard and data visualization
- **GitHub** — Project version control and portfolio presentation

## Dataset

The project uses an insurance claims dataset containing **15,420 claim records**.

The dataset includes information related to:

- Vehicle characteristics
- Policy type
- Accident details
- Driver rating
- Fault information
- Police report and witness information
- Previous claims
- Vehicle price and age
- Policyholder age
- Supplements
- Address changes
- Fraud classification

## Project Workflow

1. **Data Inspection** — Examined the dataset structure, columns, data types, and records.
2. **Data Cleaning** — Checked missing values and duplicates and converted selected categorical ranges into numeric features.
3. **Exploratory Data Analysis** — Analyzed fraud patterns across important claim characteristics.
4. **Visualization** — Created charts to understand fraud distribution and fraud rates.
5. **SQLite Database** — Stored the cleaned dataset in a SQLite database.
6. **SQL Analysis** — Performed fraud-related aggregations and comparative analysis using SQL.
7. **Power BI Dashboard** — Built an interactive dashboard to present claim volume and fraud patterns.
8. **Business Insights** — Documented findings and recommendations based on the analysis.

## Key Results

- Total claims analyzed: **15,420**
- Fraudulent claims: **923**
- Non-fraudulent claims: **14,497**
- Overall fraud rate: **5.99%**
- Utility vehicles had an observed fraud rate of **11.25%**.
- Rural accident claims had an observed fraud rate of **8.32%**.
- Policy Holder fault claims had an observed fraud rate of **7.89%**.
- Claims without a police report had an observed fraud rate of **6.05%**.
- Claims without a witness had an observed fraud rate of **6.00%**.

> These are descriptive findings from the analyzed dataset and do not by themselves establish that an individual claim is fraudulent.

## Power BI Dashboard

The project includes a Power BI dashboard with two report pages.

### Page 1 — Fraud Analysis Overview

- Total Claims
- Non-Fraud Claims
- Fraud Claims
- Fraud Rate
- Fraud vs Non-Fraud distribution
- Fraud Claims by Vehicle Category
- Fraud Claims by Policy Type
- Fraud Claims by Fault

### Page 2 — Fraud Risk Analysis

- Fraud Claims by Accident Area
- Fraud Rate by Vehicle Category
- Fraud Rate by Policy Type
- Fraud Rate by Accident Area
- Fraud Rate by Fault
- Fraud Rate by Driver Rating

## Project Structure

```text
Insurance_Claims_Analysis/
│
├── data/
│   ├── raw/
│   │   └── fraud_oracle.csv
│   └── cleaned/
│       └── fraud_oracle_cleaned.csv
│
├── documentation/
│   └── business_insights.md
│
├── images/
│   └── fraud analysis charts
│
├── powerbi/
│   └── Fraud_data_analysis.pbix
│
├── python/
│   ├── 01_data_inspection.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   ├── 04_visualization.py
│   ├── 05_create_sqlite_db.py
│   ├── 06_test_sqlite.py
│   └── 07_run_sql.py
│
├── sql/
│   ├── 01_fraud_analysis.sql
│   └── insurance_claims.db
│
└── README.md


## Business Insights

The analysis identified several patterns in the observed fraud rates:

- Fraud rates varied across vehicle categories, with Utility vehicles showing a higher observed rate than Sedan and Sport vehicles.
- Rural accident claims had a higher observed fraud rate than Urban accident claims.
- Policy Holder fault claims had a higher observed fraud rate than Third Party fault claims.
- Fraud rates were relatively similar across the four Driver Rating groups.
- Claims without a police report or witness had higher observed fraud rates than claims with these records.
- The observed fraud rate varied across vehicle-price and vehicle-age categories.
- Policyholder age groups showed noticeable differences in observed fraud rates.
- Address-change categories showed different observed fraud rates, but very small groups should be interpreted cautiously.

## Documentation

Detailed business findings and observations are available in:

`documentation/business_insights.md`

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Insurance_Claims_Analysis

python python/01_data_inspection.py
python python/02_data_cleaning.py
python python/03_eda.py
python python/04_visualization.py
python python/05_create_sqlite_db.py
python python/06_test_sqlite.py
python python/07_run_sql.py


### One thing I'd remove for now

Don't include:

```bash
git clone <your-github-repository-url>

## Limitations

- The analysis is based on the available historical insurance claims dataset.
- Observed fraud-rate differences describe patterns in the dataset and do not prove that a specific claim is fraudulent.
- Some categories contain relatively few records, so their fraud rates should be interpreted cautiously.
- The Power BI dashboard is intended for analytical and reporting purposes rather than automated fraud-decision making.

## Skills Demonstrated

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Python & Pandas
- Data Visualization
- SQL & SQLite
- Power BI Dashboard Development
- Business Insight Generation
- Data Analysis & Reporting