#!/usr/bin/env python3
"""Perform Welch's t-tests on numerical features."""

from scipy import stats


def ttest_numeric(df):
    """Calculate Welch's t-test p-values for numeric columns."""
    results = {}

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        churn_yes = df[df["Churn"] == "Yes"][col].dropna()
        churn_no = df[df["Churn"] == "No"][col].dropna()

        t_stat, p_value = stats.ttest_ind(
            churn_yes,
            churn_no,
            equal_var=False
        )

        results[col] = p_value

    return results
