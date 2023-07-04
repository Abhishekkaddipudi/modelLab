import pytest
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from modelLab.Regression.regression_metrics import calculate_metrics
from modelLab.Regression.regression import RegressionChecker


@pytest.fixture
def example_data():
    # Example test data
    y_true = np.array([1, 2, 3, 4, 5])
    y_pred = np.array([1.2, 2.1, 2.9, 4.2, 4.8])
    n_features = 2
    return y_true, y_pred, n_features

def test_calculate_metrics(example_data):
    y_true, y_pred, n_features = example_data

    # Calculate expected metric values using sklearn's functions
    expected_adjusted_r2 = 1 - ((1 - r2_score(y_true, y_pred)) * (len(y_true) - 1)) / (len(y_true) - n_features - 1)
    expected_r2 = r2_score(y_true, y_pred)
    expected_mse = mean_squared_error(y_true, y_pred)
    expected_rmse = np.sqrt(expected_mse)
    expected_mae = mean_absolute_error(y_true, y_pred)

    # Call the function to calculate metrics
    metrics = calculate_metrics(y_true, y_pred, n_features)

    # Check if the calculated metrics match the expected values
    assert metrics['Adjusted R^2'] == expected_adjusted_r2
    assert metrics['R^2'] == expected_r2
    assert metrics['MSE'] == expected_mse
    assert metrics['RMSE'] == expected_rmse
    assert metrics['MAE'] == expected_mae


import pytest
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

@pytest.fixture
def example_data1():
    # Example test data
    X, y = make_regression(n_samples=100, n_features=10, random_state=42)
    return X, y

def test_RegressionChecker(example_data1):
    X, y = example_data1

    # Define the regression models to evaluate
    models = {
        'Linear Regression': LinearRegression()
    }

    # Create an instance of RegressionChecker
    checker = RegressionChecker(models)

    # Fit the models using the test data
    checker.fit_models(X, y)

    # Get the evaluation results
    results = checker.get_results()

    # Check if the results dictionary contains the expected keys
    assert set(results.keys()) == set(models.keys())

    # Check if the results dictionary values are dictionaries containing evaluation metrics
    for model_name, metrics in results.items():
        assert isinstance(metrics, dict)
        assert all(metric_name in metrics for metric_name in ['Adjusted R^2', 'R^2', 'MSE', 'RMSE', 'MAE'])
