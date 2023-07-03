from modelLab import regressors
from sklearn.datasets import fetch_california_housing
import warnings
warnings.filterwarnings('ignore')
X,y=fetch_california_housing(return_X_y=True)

regressors(X,y,verbose=True)