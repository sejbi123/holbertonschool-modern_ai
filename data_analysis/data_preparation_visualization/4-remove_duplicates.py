#!/usr/bin/env python3
import pandas as pd


def remove_duplicates(df):
    """Remove duplicate rows, keeping the first occurrence"""
    df = df.drop_duplicates()

    """Return the DataFrame without duplicates"""
    return df
