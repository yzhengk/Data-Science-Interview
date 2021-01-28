from sklearn.linear_model import Ridge
ridge = Ridge(alpha = 1.0)

from sklearn.linear_model import Lasso
lasso = Lasso(alpha = 1.0)

from sklearn.linear_model import ElasticNet
elanet = ElasticNet(alpha = 1.0, l1_ratio = 0.5)
