# 🔢 Linear Regression — Scratch to scikit-learn

This project demonstrates **Linear Regression** using:
1. ✅ Scikit-learn (library-based)
2. 🔧 Gradient Descent (from scratch)
3. 🧮 Least Squares (analytical method)

We use a simple synthetic dataset generated from the equation:
y = 2.5x + 5 + noise

---

## 📁 Project Structure
.
├── data/
│   └── dataset.csv             # Synthetic data (x, y)
├── models/
│   ├── sklearn_model.py        # Scikit-learn regression
│   ├── gradient_descent.py     # Gradient descent
│   └── least_squares.py        # Least squares
├── generate_data.py            # Script to create dataset
├── main.py                     # Runs all three models & plots
├── plots/
│   └── regression_plot.png     # Output plot comparing models
├── README.md
└── requirements.txt