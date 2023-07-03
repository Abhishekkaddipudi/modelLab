from modelLab import classifier
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')
X,y=load_iris(return_X_y=True)

classifier(X,y,verbose=True)