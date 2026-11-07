#!/usr/bin/env python3
"""Visualize correlations between numerical features."""

import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """Create a heatmap to show correlations between numeric features."""
    plt.figure(figsize=(6, 5))

    numeric_df = df.select_dtypes(include="number")
    corr_matrix = numeric_df.corr()

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        vmin=-1,
        vmax=1
    )

    plt.title("Correlation Matrix")
    plt.show()

    return None
