import pandas as pd
from sklearn.datasets import fetch_california_housing
import os

# Create data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Load California Housing dataset
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['price'] = data.target

# Save dataset to CSV
df.to_csv("data/housing.csv", index=False)
print("Dataset saved to data/housing.csv")
