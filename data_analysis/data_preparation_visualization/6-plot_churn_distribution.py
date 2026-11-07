#!/usr/bin/env python3
"""Plot churn distribution."""

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Visualize the distribution of churn classes."""
    plt.figure(figsize=(12, 8))

    counts = df["Churn"].value_counts()
    counts = counts.reindex(["No", "Yes"], fill_value=0)

    plt.bar(
        counts.index,
        counts.values,
        color=["skyblue", "salmon"]
    )

    plt.title("Churn Distribution")
    plt.ylabel("Count")
    plt.xlabel("")

    plt.show()
    return None
