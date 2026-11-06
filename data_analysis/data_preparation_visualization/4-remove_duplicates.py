#!/usr/bin/env python3
"""Remove duplicate rows from a DataFrame."""


def remove_duplicates(df):
    """Remove duplicate rows, keeping the first occurrence."""
    df = df.drop_duplicates()

    return df
