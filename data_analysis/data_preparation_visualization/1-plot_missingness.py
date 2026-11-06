#!/usr/bin/env python3
"""
Visualize missing values in a DataFrame.
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    Plot missing values using vertical markers.
    """
    plt.figure(figsize=(12, 8))

    missing = df.isnull()
    rows, cols = np.where(missing)

    plt.scatter(rows, cols, marker='|')

    plt.yticks(range(len(df.columns)), df.columns)
    plt.xlim(-0.5, len(df) - 0.5)
    plt.ylim(-0.5, len(df.columns) - 0.5)

    plt.tight_layout()
    plt.show()
    