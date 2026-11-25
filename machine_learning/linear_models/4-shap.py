#!/usr/bin/env python3
"""SHAP explainability module."""
import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """
    Create a SHAP explainer and compute SHAP values for X_test.

    Args:
        model: a trained regression model
        X_train: input data used as the background dataset
        X_test: input data to explain

    Returns:
        explainer: the SHAP explainer object
        shap_values: SHAP values (Explanation) for the predictions on X_test
    """
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
