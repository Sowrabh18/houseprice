## Status
- Initialized Git repository and set up `.gitignore`.
- Initialized DVC and versioned the California Housing dataset.
- Created DVC pipeline for data loading.
- Trained linear regression model and logged with MLflow.
- Versioned model with DVC.

## Setup
1. Install dependencies: `pip install dvc mlflow scikit-learn pandas numpy joblib`
2. Clone repo: `git clone https://github.com/your-username/house-price-mlops.git`
3. Run pipeline: `dvc repro`
4. View MLflow experiments: `mlflow ui`

## Structure
- `data/`: Dataset and loading script
- `src/`: Training script
- `models/`: Trained model
- `dvc.yaml`: DVC pipeline configuration
- `.gitignore`: Ignored files
- `README.md`: Project documentation

