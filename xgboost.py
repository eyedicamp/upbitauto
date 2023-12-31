from sklearn.datasets import load_iris
import xgboost
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score
from get_trade_price import change_rate

X_train, X_test, y_train, y_test = train_test_split(change_rate,test_size=0.1)
xgb_model = xgboost.XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,
                           colsample_bytree=1, max_depth=7)

print(len(X_train), len(X_test))
xgb_model.fit(X_train,y_train)

xgboost.plot_importance(xgb_model)

predictions = xgb_model.predict(X_test)
print(predictions)

r_sq = xgb_model.score(X_train, y_train)
print(r_sq)
print(explained_variance_score(predictions,y_test))