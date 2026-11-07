#!/usr/bin/env python3
"""Plot numeric features by churn."""

import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """Plot a numeric feature by churn."""
    plt.figure(figsize=(12, 8))

    no_churn = df[df["Churn"] == "No"][col]

    yes_churn = df[df["Churn"] == "Yes"][col]

    plt.hist(
        [
            no_churn,
            yes_churn
        ],
        bins=30,
        label=["No", "Yes"]
    )

    plt.title("{} Distribution by Churn".format(col))
    plt.xlabel(col)
    plt.legend(title="Churn")

    plt.show()
    