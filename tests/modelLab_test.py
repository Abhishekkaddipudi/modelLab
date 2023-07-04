import pytest
import numpy as np
from sklearn.datasets import make_regression, make_classification
from sklearn.linear_model import LinearRegression, LogisticRegression
from modelLab import regressors,classifier
from modelLab.initial_checks import check_data

@pytest.fixture
def example_regression_data():
    # Example test data for regression
    X, y = make_regression(n_samples=100, n_features=10, random_state=42)
    return X, y

@pytest.fixture
def example_classification_data():
    # Example test data for classification
    X, y = make_classification(n_samples=100, n_features=10, random_state=42)
    return X, y

def test_regressors(example_regression_data):
    X, y = example_regression_data

    # Define the regression models to evaluate
    models = {
        'Linear Regression': LinearRegression()
    }

    # Test the regressors function
    results = regressors(X, y, models=models, verbose=False, rets=True)

    # Check if the results dictionary contains the expected keys
    assert set(results.keys()) == set(models.keys())

    # Check if the results dictionary values are dictionaries containing evaluation metrics
    for model_name, metrics in results.items():
        assert isinstance(metrics, dict)
        assert all(metric_name in metrics for metric_name in ['Adjusted R^2', 'R^2', 'MSE', 'RMSE', 'MAE'])


def test_classifier(example_classification_data):
    X, y = example_classification_data

    # Define the classification models to evaluate
    models = {
        'Logistic Regression': LogisticRegression()
    }

    # Test the classifier function
    results = classifier(X, y, models=models, verbose=False, rets=True)

    # Check if the results dictionary contains the expected keys
    assert set(results.keys()) == set(models.keys())

    # Check if the results dictionary values are dictionaries containing evaluation metrics
    for model_name, metrics in results.items():
        assert isinstance(metrics, dict)
        assert all(metric_name in metrics for metric_name in ['Accuracy', 'Precision', 'Recall', 'F1 Score'])


import pytest
import numpy as np

def test_check_data_valid():
    # Valid test data
    X = np.array([[1, 4], [2, 5], [3, 6]])
    y = np.array([1, 2, 3])

    # Test the check_data function
    result = check_data(X, y)

    # Check if the result is True
    assert result == True

def test_check_data_empty_dataset():
    # Test data with empty dataset
    X = np.array([])
    y = np.array([])

    # Check if ValueError is raised
    with pytest.raises(ValueError):
        check_data(X, y)

def test_check_data_missing_values():
    # Test data with missing values
    X = np.array([[1, 4], [np.nan, 5], [3, np.nan]])
    y = np.array([1, 2, np.nan])

    # Check if ValueError is raised
    with pytest.raises(ValueError):
        check_data(X, y)

def test_check_data_infinite_values():
    # Test data with infinite values
    X = np.array([[1, 4], [np.inf, 5], [3, 6]])
    y = np.array([1, 2, np.inf])

    # Check if ValueError is raised
    with pytest.raises(ValueError):
        check_data(X, y)
