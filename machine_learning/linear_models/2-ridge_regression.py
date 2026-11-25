#!/usr/bin/env python3
"""Dataset generation module for the feature attribution project."""
import numpy as np


def generate_data():
    """
    Generate the synthetic dataset with collinear features.

    Returns:
        X: numpy.ndarray of shape (200, 3) with columns X1, X2, X3
        y: numpy.ndarray of shape (200,) with the target values
    """
    np.random.seed(42)
    X1 = np.random.rand(200) * 10
    X2 = X1 + np.random.normal(0, 0.05, 200)
    X3 = np.random.rand(200) * 5
    X = np.column_stack([X1, X2, X3])
    y = 4 * X1 + 3 * X3 + np.random.normal(0, 5, 200)
    return X, y
    