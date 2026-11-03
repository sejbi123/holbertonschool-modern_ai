# Data Preparation and Visualization

## Description

This project focuses on data preparation, cleaning, and visualization using Python. It uses the Telco Customer Churn dataset to explore data quality, identify missing values, and prepare the dataset for further analysis.

## Tasks

### 0. Describe Data
Explore the dataset by displaying its shape, data types, first five rows, missing values, and duplicate records.

### 1. Visualize Missing Data
Create a scatter plot to visualize the positions of missing values in a DataFrame using Matplotlib.

### 2. Convert Columns
Convert the `TotalCharges` column to numeric values and transform `SeniorCitizen` values into categorical labels.

### 3. Clean Total Charges
Handle missing values in `TotalCharges` using three methods:
- Drop rows with missing values.
- Replace missing values with the median.
- Impute missing values using `MonthlyCharges * tenure`.

### 4. Remove Duplicates
Remove duplicate rows from the dataset.

### 5. Drop Customer ID
Remove the `customerID` column because it contains unique customer identifiers and is not needed for the analysis.

## Technologies

- Python 3
- Pandas
- NumPy
- Matplotlib

## Dataset

Telco Customer Churn dataset (`Telco-Customer-Churn.csv`).
