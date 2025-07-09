import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import os

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Load dataset
data = pd.read_csv("data/housing.csv")

# Prepare features and target
X = data.drop("price", axis=1)
y = data["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Log with MLflow
mlflow.set_experiment("house-price-prediction")
with mlflow.start_run():
    mlflow.log_param("test_size", 0.2)
    mlflow.log_param("random_state", 42)
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)
    mlflow.sklearn.log_model(model, "model")

# Save model
import joblib
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/linear_model.pkl")
print("Model saved to models/linear_model.pkl")