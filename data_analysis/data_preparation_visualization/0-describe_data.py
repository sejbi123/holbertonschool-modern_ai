#!/usr/bin/env python3
"""Import pandas and load the dataset."""
import pandas as pd

df = pd.read_csv('Telco-Customer-Churn.csv')

"""Extract basic information about the dataset."""
shape = df.shape
data_types = df.dtypes
head = df.head()
missing_count = df.isnull().sum()
duplicates = df.duplicated().sum()

"""Display the results."""
print("Shape:", shape)
print("Dtypes:\n", data_types)
print("First rows:\n", head)
print("Missing values:\n", missing_count)
print("Duplicates:", duplicates)
