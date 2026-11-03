#!/usr/bin/env python3
"""Visualize missing values in a pandas DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Create a scatter plot showing the positions of missing values."""
    plt.figure(figsize=(12, 8))

    x, y = np.where(df.isnull())

    plt.scatter(x, y, marker='|')

    plt.yticks(np.arange(len(df.columns)), df.columns)

    plt.tight_layout()
    plt.show()
