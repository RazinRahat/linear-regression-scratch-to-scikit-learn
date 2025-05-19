# 🔢 Linear Regression — Scratch to scikit-learn

This project demonstrates **Linear Regression** using:
1. ✅ Scikit-learn (library-based)
2. 🔧 Gradient Descent (from scratch)
3. 🧮 Least Squares (analytical method)

We use a simple synthetic dataset generated from the equation:
y = 2.5x + 5 + noise

---

## 📁 Project Structure
<pre>
linear-regression-three-ways/
├── data/
│   └── dataset.csv              # Generated synthetic dataset
├── models/
│   ├── sklearn_model.py         # Linear regression using Scikit-learn
│   ├── gradient_descent.py      # Linear regression using gradient descent (from scratch)
│   └── least_squares.py         # Linear regression using least squares (analytical method)
├── plots/
│   └── regression_plot.png      # Output plot comparing all three models
├── generate_data.py             # Script to generate synthetic dataset
├── main.py                      # Runs all models, compares results, and plots them
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
</pre>
