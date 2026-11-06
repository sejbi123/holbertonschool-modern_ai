#!/usr/bin/env python3
"""Visualize missing values in a DataFrame."""

import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Plot the positions of missing values in the DataFrame."""
    plt.figure(figsize=(12, 8))

    missing = df.isna().values
    rows, cols = np.where(missing)

    plt.scatter(rows, cols, marker='|')

    plt.yticks(np.arange(len(df.columns)), df.columns)
    plt.xlabel('Row Index')
    plt.ylabel('Column Names')

    plt.tight_layout()
    plt.show()

    return None
