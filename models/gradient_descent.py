import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

def run_gradient_descent(data_path='data/dataset.csv', learning_rate=0.01, epochs=1000):
    df = pd.read_csv(data_path)
    X = df['x'].values
    y = df['y'].values
    n = len(X)

    w = 0.0
    b = 0.0

    for _ in range(epochs):
        y_pred = w * X + b
        error = y_pred - y

        dw = (2/n) * np.dot(error, X)
        db = (2/n) * np.sum(error)

        w -= learning_rate * dw
        b -= learning_rate * db

    final_preds = w * X + b
    mse = mean_squared_error(y, final_preds)

    return w, b, mse, final_preds