#!/usr/bin/env python3
"""Plot numeric feature distributions based on churn categories."""

import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """Display the distribution of a numeric feature for each churn category."""
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
    