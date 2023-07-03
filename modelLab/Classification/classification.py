from sklearn.exceptions import NotFittedError
from sklearn.model_selection import KFold
from .classification_metrics import calculate_metrics
from collections import defaultdict
from sklearn.preprocessing import StandardScaler


class ClassificationChecker:
    """
    A class for evaluating classification models.

    Args:
        models (dict): A dictionary containing the classification models to evaluate.
        scaled (bool, optional): Indicates whether to scale the input features using StandardScaler. Default is False.
        n_splits (int, optional): The number of folds for cross-validation. Default is 5.
        random_state (int, optional): The random seed for reproducibility. Default is 42.

    Attributes:
        models (dict): A dictionary containing the classification models to evaluate.
        results (defaultdict): A defaultdict object to store the evaluation results.
        n_splits (int): The number of folds for cross-validation.
        random_state (int): The random seed for reproducibility.
        scaled (bool): Indicates whether the input features should be scaled using StandardScaler.

    Methods:
        fit_models(X, y): Fits the classification models to the given data.
        get_results(): Retrieves the evaluation results.

    """
    def __init__(self, models, scaled=False, n_splits=5, random_state=42):
        """
        Initialize the RegressionChecker object.

        Args:
            models (dict): A dictionary of regression models to evaluate.
            scaled (bool, optional): Indicates whether to perform feature scaling using StandardScaler. Default is False.
            n_splits (int, optional): The number of splits for cross-validation. Default is 5.
            random_state (int, optional): The random state for reproducible results. Default is 42.

        """
        self.models = models
        self.results = defaultdict(dict)
        self.n_splits = n_splits
        self.random_state = random_state
        self.scaled=scaled

    def fit_models(self, X, y):
        """
        Fits the classification models to the given data.

        Args:
            X (array-like): The input features.
            y (array-like): The target variable.

        """
        kf = KFold(n_splits=self.n_splits, shuffle=True, random_state=self.random_state)

        for train_index, test_index in kf.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

            scaler = StandardScaler()
            if not self.scaled:
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
            else:
                X_train_scaled = X_train
                X_test_scaled = X_test

            for model_name, model in self.models.items():
                try:
                    model.fit(X_train_scaled, y_train)
                    y_pred = model.predict(X_test_scaled)
                    metrics = calculate_metrics(y_test, y_pred)
                    self.results[model_name]=(metrics)
                    del y_pred  # Clear the memory after use
                except NotFittedError:
                    print(f"Model '{model_name}' has not been fitted. Skipping evaluation.")
                finally:
                    del model  # Clear the memory after use
                    # Clear the memory after use

    def get_results(self):
        """
        Retrieves the evaluation results.

        Returns:
            dict: A dictionary containing the evaluation results for each model.

        """
        return self.results