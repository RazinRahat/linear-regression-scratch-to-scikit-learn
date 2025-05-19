import pandas as pd
import matplotlib.pyplot as plt
import os

from models.sklearn_model import run_sklearn_model
from models.gradient_descent import run_gradient_descent
from models.least_squares import run_least_squares

os.makedirs("plots", exist_ok=True)

df = pd.read_csv('data/dataset.csv')
X = df['x'].values
y = df['y'].values

w_skl, b_skl, mse_skl, y_skl = run_sklearn_model()
w_gd, b_gd, mse_gd, y_gd = run_gradient_descent()
w_ls, b_ls, mse_ls, y_ls = run_least_squares()

print("🔍 Model Results:")
print(f"Scikit-learn     → w = {w_skl:.2f}, b = {b_skl:.2f}, MSE = {mse_skl:.2f}")
print(f"Gradient Descent → w = {w_gd:.2f}, b = {b_gd:.2f}, MSE = {mse_gd:.2f}")
print(f"Least Squares    → w = {w_ls:.2f}, b = {b_ls:.2f}, MSE = {mse_ls:.2f}")

sorted_indices = X.argsort()
X_sorted = X[sorted_indices]
y_skl_sorted = y_skl[sorted_indices]
y_gd_sorted = y_gd[sorted_indices]
y_ls_sorted = y_ls[sorted_indices]

def plot_model(X, y, y_pred, model_name, color):
    plt.figure(figsize=(8, 5))
    plt.scatter(X, y, color='gray', label='Data', alpha=0.6)
    plt.plot(X, y_pred, color=color, label=model_name)
    plt.title(f"Linear Regression: {model_name}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    filename = f"plots/regression_{model_name.lower().replace(' ', '_')}.png"
    plt.savefig(filename)
    plt.close()

plot_model(X_sorted, y, y_skl_sorted, "Scikit-learn", "blue")
plot_model(X_sorted, y, y_gd_sorted, "Gradient Descent", "green")
plot_model(X_sorted, y, y_ls_sorted, "Least Squares", "red")