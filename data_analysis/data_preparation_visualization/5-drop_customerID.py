#!/usr/bin/env python3
"""Drop the customerID column from the DataFrame."""


def drop_customerID(df):
    """Remove the customerID column and return the DataFrame."""
    df = df.drop(columns=['customerID'])

    return df
