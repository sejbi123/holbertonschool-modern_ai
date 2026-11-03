#!/usr/bin/env python3
import pandas as pd


def drop_customerID(df):
    """Drop the customerID column because it contains unique customer identifiers"""
    df = df.drop(columns=['customerID'])

    # Return the updated DataFrame
    return df
