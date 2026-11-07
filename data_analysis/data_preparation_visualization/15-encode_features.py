#!/usr/bin/env python3
"""Transform categorical variables into numerical representations."""

import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode categorical features and return the fitted encoders."""
    df = df.copy()

    # Convert Churn labels into numerical values
    churn_le = preprocessing.LabelEncoder()
    df["Churn"] = churn_le.fit_transform(df["Churn"])

    # Apply ordinal encoding to binary categorical columns
    binary_cols = [
        "Partner",
        "Dependents",
        "PaperlessBilling",
        "SeniorCitizen"
    ]

    binary_oe = preprocessing.OrdinalEncoder(
        categories=[["No", "Yes"]]
    )

    for col in binary_cols:
        df[[col]] = binary_oe.fit_transform(
            df[[col]]
        ).astype(int)

    # Apply ordinal encoding to TenureGroup
    tenure_oe = preprocessing.OrdinalEncoder()

    df[["TenureGroup"]] = tenure_oe.fit_transform(
        df[["TenureGroup"]]
    ).astype(int)

    # Apply one-hot encoding to Contract and PaymentMethod
    df = pd.get_dummies(
        df,
        columns=["Contract", "PaymentMethod"],
        drop_first=True,
        dtype=int
    )

    return df, churn_le, binary_oe, tenure_oe
