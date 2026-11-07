#!/usr/bin/env python3
"""
Module for plotting the distribution of customer churn.
"""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    Plot the distribution of customers based on their churn status.
    """
    plt.figure(figsize=(12, 8))

    churn_counts = df['Churn'].value_counts().reindex(['No', 'Yes'])

    plt.bar(
        churn_counts.index,
        churn_counts.values,
        color=['skyblue', 'salmon']
    )

    plt.title('Churn Distribution')
    plt.xlabel('Churn')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.show()
    