#!/usr/bin/env python3
"""Module for creating a linear regression model."""

from sklearn import linear_model


def Linear_Regression():
    """Create and return an untrained Linear Regression model."""
    return linear_model.LinearRegression()
