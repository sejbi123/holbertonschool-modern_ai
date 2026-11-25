#!/usr/bin/env python3
"""Ridge Regression module."""
from sklearn import linear_model


def ridge_regression(random_state):
    """
    Create a Ridge Regression model.

    Args:
        random_state: integer used to set the random seed

    Returns:
        An untrained Ridge regression model instance
    """
    return linear_model.Ridge(random_state=random_state)
