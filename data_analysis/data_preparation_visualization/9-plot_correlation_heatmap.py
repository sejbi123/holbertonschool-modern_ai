#!/usr/bin/env python3
"""Visualize relationships between numerical features using a correlation heatmap."""

import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """Generate a heatmap to illustrate correlations among numerical features."""
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
