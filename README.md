[![Unit Test](https://github.com/Abhishekkaddipudi/modelLab/actions/workflows/main.yml/badge.svg)](https://github.com/Abhishekkaddipudi/modelLab/actions/workflows/main.yml)
<a href=""><img src="https://img.shields.io/badge/Version-V0.0.1-blue.svg"/></a>
<a href=""><img src="https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue.svg"/></a>
---

**modelLab** is a comprehensive library of  machine learning models designed to facilitate regression or classification tasks on a given dataset. It encompasses a diverse range of models and provides a comprehensive evaluation of each model's performance, delivering a comprehensive set of metrics in a Python dictionary.

### PURPOSE OF THE PACKAGE
- The primary objective of the package is to offer a curated ensemble of renowned scikit-learn models, enabling users to conveniently train all models with a single function call.

### FEATURES
+ Collections of Machine learning models

    + **Classification Models**                                                          
    
        -   'LinearSVC'
        -   'SGDClassifier'
        -   'MLPClassifier'
        -   'Perceptron'
        -   'LogisticRegression'
        -   'LogisticRegressionCV'
        -   'SVC'
        -   'CalibratedClassifierCV'
        -   'PassiveAggressiveClassifier'
        -   'LabelPropagation'
        -   'LabelSpreading'
        -   'RandomForestClassifier'
        -   'GradientBoostingClassifier'
        -   'QuadraticDiscriminantAnalysis'
        -   'HistGradientBoostingClassifier'
        -   'RidgeClassifierCV'
        -   'RidgeClassifier'
        -   'AdaBoostClassifier'
        -   'ExtraTreesClassifier'
        -   'KNeighborsClassifier'
        -   'BaggingClassifier'
        -   'BernoulliNB'
        -   'LinearDiscriminantAnalysis'
        -   'GaussianNB'
        -   'NuSVC'
        -   'DecisionTreeClassifier'
        -   'NearestCentroid'
        -   'ExtraTreeClassifier'
        -   'DummyClassifier'
          
    +  **Regression Models**
      
        -   'SVR'
        -   'RandomForestRegressor'
        -   'ExtraTreesRegressor'
        -   'AdaBoostRegressor'
        -   'NuSVR'
        -   'GradientBoostingRegressor'
        -   'KNeighborsRegressor'
        -   'HuberRegressor'
        -   'RidgeCV'
        -   'BayesianRidge'
        -   'Ridge'
        -   'LinearRegression'
        -   'LarsCV'
        -   'MLPRegressor'
        -   'XGBRegressor'
        -   'CatBoostRegressor'
        -   'LGBMRegressor'
     

### GETTING STARTED
This package is available on PyPI, allowing for convenient installation through the PyPI repository.

### Dependencies
    -  'scikit-learn'
    -  'xgboost'
    -  'catboost'
    -  'lightgbm'
### INSTALLATION

If you already installed scikit-learn, the easiest way to install modelLab is using ``pip``:

```bash
pip install modelLab
```

### USAGE 
```python
>>> from modelLab import regressors,classifier
>>> regressors(X, y, models=models, verbose=False, rets=True) #X,y is data
>>> classifier(X, y, models=models, verbose=False, rets=True)
```
### Examples

+ Classification Problem
  
```python
>>> from modelLab import regressors,classifier
>>> from sklearn.datasets import load_iris
>>> X,y=load_iris(return_X_y=True)
>>> import warnings                           
>>> warnings.filterwarnings('ignore')
>>> classifier(X,y,verbose=True)              
Model: LinearSVC
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: SGDClassifier
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9661

Model: MLPClassifier
Accuracy: 1.0000
Precision: 1.0000
Recall: 1.0000
F1 Score: 1.0000

Model: Perceptron
Accuracy: 0.8667
Precision: 0.9022
Recall: 0.8667
F1 Score: 0.8626

Model: LogisticRegression
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: SVC
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: CalibratedClassifierCV
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: PassiveAggressiveClassifier
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: LabelPropagation
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: LabelSpreading
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: RandomForestClassifier
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: GradientBoostingClassifier
Accuracy: 0.9333
Precision: 0.9436
Recall: 0.9333
F1 Score: 0.9331

Model: QuadraticDiscriminantAnalysis
Accuracy: 1.0000
Precision: 1.0000
Recall: 1.0000
F1 Score: 1.0000

Model: HistGradientBoostingClassifier
Accuracy: 0.9000
Precision: 0.9214
Recall: 0.9000
F1 Score: 0.8989

Model: RidgeClassifierCV
Accuracy: 0.8667
Precision: 0.8754
Recall: 0.8667
F1 Score: 0.8662

Model: RidgeClassifier
Accuracy: 0.8667
Precision: 0.8754
Recall: 0.8667
F1 Score: 0.8662

Model: AdaBoostClassifier
Accuracy: 0.9333
Precision: 0.9436
Recall: 0.9333
F1 Score: 0.9331

Model: ExtraTreesClassifier
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: KNeighborsClassifier
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: BaggingClassifier
Accuracy: 0.9333
Precision: 0.9436
Recall: 0.9333
F1 Score: 0.9331

Model: BernoulliNB
Accuracy: 0.2333
Precision: 0.0544
Recall: 0.2333
F1 Score: 0.0883

Model: LinearDiscriminantAnalysis
Accuracy: 1.0000
Precision: 1.0000
Recall: 1.0000
F1 Score: 1.0000

Model: GaussianNB
Accuracy: 0.9333
Precision: 0.9333
Recall: 0.9333
F1 Score: 0.9333

Model: NuSVC
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: DecisionTreeClassifier
Accuracy: 0.9333
Precision: 0.9436
Recall: 0.9333
F1 Score: 0.9331

Model: NearestCentroid
Accuracy: 0.9000
Precision: 0.9025
Recall: 0.9000
F1 Score: 0.9000

Model: ExtraTreeClassifier
Accuracy: 0.9667
Precision: 0.9694
Recall: 0.9667
F1 Score: 0.9667

Model: DummyClassifier
Accuracy: 0.2333
Precision: 0.0544
Recall: 0.2333
F1 Score: 0.0883
```
+ Using Custom Models
  
```python
>>> from sklearn.datasets import make_regression
>>> from sklearn.linear_model import LinearRegression
>>> from modelLab import regressors
>>> X, y = make_regression(n_samples=100, n_features=10, random_state=42)
>>> models = {'Linear Regression': LinearRegression()}
>>> regressors(X, y, models=models, verbose=False, rets=True)
defaultdict(<class 'dict'>, {'Linear Regression': {'Adjusted R^2': 1.0, 'R^2': 1.0, 'MSE': 3.097635893749451e-26, 'RMSE': 1.7600101970583725e-13, 'MAE': 1.4992451724538115e-13}})
```

```python
>>> from sklearn.datasets import make_regression, make_classification
>>> from sklearn.linear_model import LogisticRegression
>>> from modelLab import classifier
>>> X, y = make_classification(n_samples=100, n_features=10, random_state=42)
>>> models = {'Logistic Regression': LogisticRegression()}  
>>> classifier(X, y, models=models, verbose=False, rets=True)
defaultdict(<class 'dict'>, {'Logistic Regression': {'Accuracy': 0.95, 'Precision': 0.9545454545454545, 'Recall': 0.95, 'F1 Score': 0.949874686716792}})
```



