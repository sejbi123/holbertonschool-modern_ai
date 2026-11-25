#!/usr/bin/env python3
"""Lasso Regression module."""
from sklearn import linear_model


def lasso_regression(random_state):
    """
    Create a Lasso Regression model.

    Args:
        random_state: integer used to set the random seed

    Returns:
        An untrained Lasso regression model instance
    """
    return linear_model.Lasso(random_state=random_state)
