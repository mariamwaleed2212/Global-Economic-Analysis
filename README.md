 #Global Economic Analysis

## Project Overview

This project analyzes economic indicators across countries from 2010 to 2023.

The analysis focuses on GDP, GDP per capita, GDP growth, inflation, unemployment, current account balance, and Gross National Income.

## Dataset

The original dataset contains economic indicators for countries from 2010 to 2025 and was obtained from Kaggle.

For the final analysis, the data was limited to 2010–2023 because of the high level of missing data in the later years.

The cleaned dataset contains:

- 217 countries
- 14 years
- 3,038 observations
- 11 retained variables

## Data Cleaning

The following steps were performed:

- Removed observations for years after 2023.
- Removed indicators with a high percentage of missing values.
- Checked data availability.
- Calculated basic descriptive statistics.
- Created a cleaned dataset for analysis and Power BI.
- Remaining missing values were kept rather than artificially filled.

## Tools Used

- Python
- Pandas
- Matplotlib
- Power BI

## Python Analysis

Python was used to calculate country-level average values and identify the top 10 countries for:

- Average GDP
- Average GDP Growth
- Average Inflation
- Average Unemployment
- Average Current Account Balance

## Power BI Dashboard

The Power BI dashboard provides an interactive view of the economic indicators and allows comparisons between countries.

The dashboard includes:

- Total countries
- Years covered
- Top 10 average GDP
- Top 10 average GDP growth
- Top 10 average inflation
- Top 10 average unemployment
- Top 10 average current account balance
- Country filter

## Key Findings

- The United States has the highest average GDP.
- Guyana has the highest average GDP growth.
- Zimbabwe has the highest average inflation.
- Eswatini has the highest average unemployment.
- Timor-Leste has the highest average current account balance.

## Project Files

- `world_bank_data_2025.csv` – Original dataset
- `cleaned_economic_data.csv` – Cleaned dataset
- `data_analysis.py` – Python data cleaning and analysis
- `Global_Economic_Analysis.pbix` – Power BI dashboard
- `Global_Economic_Analysis_Presentation.pptx` – Project presentation
