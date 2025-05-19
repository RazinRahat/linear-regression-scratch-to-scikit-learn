import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

def run_least_squares(data_path='data/dataset.csv'):
    df = pd.read_csv(data_path)
    X = df['x'].values
    y = df['y'].values

    x_mean = np.mean(X)
    y_mean = np.mean(y)

    numerator = np.sum((X - x_mean) * (y - y_mean))
    denominator = np.sum((X - x_mean) ** 2)
    w = numerator / denominator
    b = y_mean - w * x_mean

    y_pred = w * X + b
    mse = mean_squared_error(y, y_pred)

    return w, b, mse, y_pred