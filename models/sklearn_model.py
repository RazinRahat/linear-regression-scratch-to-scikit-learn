import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def run_sklearn_model(data_path='data/dataset.csv'):
    df = pd.read_csv(data_path)
    X = df[['x']]
    y = df['y']

    model = LinearRegression()
    model.fit(X, y)

    w = model.coef_[0]     # Slope
    b = model.intercept_   # Intercept

    y_pred = model.predict(X)

    mse = mean_squared_error(y, y_pred)

    return w, b, mse, y_pred