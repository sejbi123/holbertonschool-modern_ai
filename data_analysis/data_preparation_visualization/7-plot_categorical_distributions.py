#!/usr/bin/env python3
"""Visualize categorical feature distributions."""

import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Plot categorical distributions in a grid."""
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(
            include=['object']
        ).columns.drop('Churn').tolist()
    else:
        columns_to_plot = list(columns_to_plot)

    if not columns_to_plot:
        return None

    n_cols = 3
    n_rows = (len(columns_to_plot) + n_cols - 1) // n_cols

    fig, axes = plt.subplots(
        n_rows, n_cols, figsize=(15, 5 * n_rows)
    )

    axes = axes.flatten()

    for i, col in enumerate(columns_to_plot):
        counts = df[col].value_counts()

        axes[i].bar(counts.index, counts.values)
        axes[i].set_title(col)
        axes[i].tick_params(axis='x', rotation=45)

    for j in range(len(columns_to_plot), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()

    return None
