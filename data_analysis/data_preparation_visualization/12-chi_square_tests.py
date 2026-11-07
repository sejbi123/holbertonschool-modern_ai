#!/usr/bin/env python3
"""Perform chi-square tests on categorical features."""

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Calculate chi-square p-values for categorical features."""
    results = {}

    categorical_cols = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for col in categorical_cols:
        if col == "Churn":
            continue

        contingency_table = pd.crosstab(df[col], df["Churn"])

        chi2, p_value, dof, expected = stats.chi2_contingency(
            contingency_table
        )

        results[col] = p_value

    return results
