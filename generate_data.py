import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

np.random.seed(42)

X = np.linspace(0, 10, 100)
noise = np.random.normal(0, 2, size=X.shape)
y = 2.5 * X + 5 + noise

df = pd.DataFrame({
    'x': X,
    'y': y
})

os.makedirs("data", exist_ok=True)
df.to_csv("data/dataset.csv", index=False)
print("✅ Synthetic dataset saved to 'data/dataset.csv'")
