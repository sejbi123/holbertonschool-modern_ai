#!/usr/bin/env python3
"""
Module for plotting categorical feature distributions.
"""
import math
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Plot the distributions of categorical features in a grid.
    """
    if columns_to_plot is None:
        columns_to_plot = [
            col for col in df.select_dtypes(include='object').columns
            if col != 'Churn'
        ]

    n_cols = 3
    n_rows = math.ceil(len(columns_to_plot) / n_cols)

    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=(15, 5 * n_rows)
    )

    axes = axes.flatten()

    for i, column in enumerate(columns_to_plot):
        value_counts = df[column].value_counts()

        axes[i].bar(
            value_counts.index.astype(str),
            value_counts.values
        )

        axes[i].set_title(f'Distribution of {column}')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Count')
        axes[i].tick_params(axis='x', rotation=45)

    for i in range(len(columns_to_plot), len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
    