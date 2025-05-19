# 🔢 Linear Regression — Scratch to Scikit-learn

This project demonstrates **Linear Regression** using three different methods:

1. ✅ **Scikit-learn** — library-based implementation  
2. 🔧 **Gradient Descent** — iterative method, implemented from scratch  
3. 🧮 **Least Squares** — closed-form analytical solution  

We use a **synthetic dataset** generated from the equation:

> 🧾 `y = 2.5x + 5 + noise`

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
│   ├── regression_sklearn.png           # Plot of scikit-learn model
│   ├── regression_gradient_descent.png # Plot of gradient descent model
│   └── regression_least_squares.png     # Plot of least squares model
├── generate_data.py             # Script to generate synthetic dataset
├── main.py                      # Runs all models, prints results, and saves plots
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
</pre>

---

## ⚙️ How to Install and Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/linear-regression-three-ways.git
cd linear-regression-three-ways

### 2. Install dependencies
```bash
pip install -r requirements.txt

### 3. Generate the dataset
```bash
python generate_data.py

### 4. Run the models
```bash
python main.py

## 🧠 Explanation of the Three Methods

<table>
  <tr>
    <th>Method</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Scikit-learn</strong></td>
    <td>Uses <code>LinearRegression</code> from the <code>sklearn.linear_model</code> module.</td>
  </tr>
  <tr>
    <td><strong>Gradient Descent</strong></td>
    <td>Iteratively minimizes Mean Squared Error (MSE) using manual updates to weights and bias.</td>
  </tr>
  <tr>
    <td><strong>Least Squares</strong></td>
    <td>Uses matrix algebra to solve for the best-fit line in one step (analytical).</td>
  </tr>
</table>