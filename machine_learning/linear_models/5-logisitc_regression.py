#!/usr/bin/env python3
"""Logistic Regression classifier module."""
from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """
    Create a Logistic Regression model for binary classification.

    Args:
        random_state: integer used to set the random seed

    Returns:
        An untrained LogisticRegression instance
    """
    return linear_model.LogisticRegression(random_state=random_state)
