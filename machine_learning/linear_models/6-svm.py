#!/usr/bin/env python3
"""SVM classifier module with selectable kernels."""
from sklearn import svm


def get_SVM_model(name, random_state):
    """
    Create an SVM classifier with the specified kernel.

    Args:
        name: kernel type, one of 'linear', 'poly' or 'rbf'
        random_state: integer used to set the random seed

    Returns:
        An untrained instance of SVC
    """
    return svm.SVC(kernel=name, random_state=random_state)
