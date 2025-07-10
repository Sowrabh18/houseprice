# Use official Python 3.9 image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the pipeline
CMD ["dvc", "repro", "&&", "mlflow", "ui", "--host", "0.0.0.0", "--port", "5000"]