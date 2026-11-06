#!/usr/bin/env python3
"""
Handle missing values in TotalCharges.
"""


def clean_total_charges(df, method='drop'):
    """
    Clean TotalCharges using the selected method.
    """
    df = df.copy()

    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])

    elif method == 'median':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['TotalCharges'].median()
        )

    elif method == 'impute':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['MonthlyCharges'] * df['tenure']
        )

    return df
