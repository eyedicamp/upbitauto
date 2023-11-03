from pycaret.regression import *
import pandas as pd




BTC_model = setup(session_id = 1, data = BTC_train, target = 'age', test_data = BTC_test, normalize = True, normalize_method = 'zscore', transformation = True, fold_strategy = 'stratifiedkfold', use_gpu = True)

models()

pycaret_regression_models = compare_models(n_select=25, sort='MAE', include=['lr', 'lasso', 'ridge', 'en', 'lar', 'llar', 'omp', 'br', 'ard', 'par', 'ransac', 'tr', 'huber', 'kr', 'svm', 'knn', 'dt', 'rf', 'et', 'ada', 'gbr', 'mlp', 'xgboost', 'lightgbm', 'catboost'])

