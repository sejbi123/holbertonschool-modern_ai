#!/usr/bin/env python3
import pandas as pd


def convert_columns(df):
    """Convert TotalCharges to numeric, replacing invalid values with NaN"""
    df['TotalCharges'] = pd.to_numeric(
        df['TotalCharges'], errors='coerce'
    )

    """Map SeniorCitizen values: 0 to No and 1 to Yes"""
    df['SeniorCitizen'] = df['SeniorCitizen'].map({
        0: 'No',
        1: 'Yes'
    })

    # Return the modified DataFrame
    return df
