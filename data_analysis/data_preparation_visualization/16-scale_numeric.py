#!/usr/bin/env python3
"""Apply standard scaling to numerical features."""

from sklearn import preprocessing


def scale_numeric(df):
    """Standardize MonthlyCharges and TotalCharges features."""
    scaler = preprocessing.StandardScaler()

    columns = ["MonthlyCharges", "TotalCharges"]

    df[columns] = scaler.fit_transform(df[columns])

    return df
