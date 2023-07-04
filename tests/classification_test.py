# from modelLab import classifier
from modelLab.Classification.classification_metrics import calculate_metrics
from modelLab.Classification.classification import ClassificationChecker
# from sklearn.datasets import load_iris
# import warnings
# warnings.filterwarnings('ignore')
# X,y=load_iris(return_X_y=True)

import pytest
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

@pytest.fixture
def example_data():
    y_true = [0, 1, 0, 1, 1]
    y_pred = [0, 0, 1, 1, 1]
    return y_true, y_pred

def test_calculate_metrics(example_data):
    y_true, y_pred = example_data

    expected_accuracy = accuracy_score(y_true, y_pred)
    expected_precision = precision_score(y_true, y_pred, average='weighted')
    expected_recall = recall_score(y_true, y_pred, average='weighted')
    expected_f1_score = f1_score(y_true, y_pred, average='weighted')

    metrics = calculate_metrics(y_true, y_pred)

    assert metrics['Accuracy'] == expected_accuracy
    assert metrics['Precision'] == expected_precision
    assert metrics['Recall'] == expected_recall
    assert metrics['F1 Score'] == expected_f1_score

import pytest
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

@pytest.fixture
def example_data1():
    # Example test data
    X, y = make_classification(n_samples=100, n_features=10, random_state=42)
    return X, y

def test_ClassificationChecker(example_data1):
    X, y = example_data1

    # Define the classification models to evaluate
    models = {
        'Logistic Regression': LogisticRegression(),
        'Decision Tree': DecisionTreeClassifier()
    }

    # Create an instance of ClassificationChecker
    checker = ClassificationChecker(models)

    # Fit the models using the test data
    checker.fit_models(X, y)

    # Get the evaluation results
    results = checker.get_results()

    # Check if the results dictionary contains the expected keys
    assert set(results.keys()) == set(models.keys())

    # Check if the results dictionary values are dictionaries containing evaluation metrics
    for model_name, metrics in results.items():
        assert isinstance(metrics, dict)
        assert all(metric_name in metrics for metric_name in ['Accuracy', 'Precision', 'Recall', 'F1 Score'])
