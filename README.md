# House Price Prediction MLOps Pipeline

A machine learning project to predict house prices using Git, DVC, MLflow, and GitHub Actions.

## Status
- Initialized Git repository and set up `.gitignore`.
- Initialized DVC and versioned the California Housing dataset.
- Created DVC pipeline for data loading.
- Trained linear regression model and logged with MLflow.
- Versioned model with DVC.
- Set up CI with GitHub Actions to run DVC pipeline.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Clone repo: `git clone https://github.com/Sowrabh18/houseprice.git`
3. Run pipeline: `dvc repro`
4. View MLflow experiments: `mlflow ui`

## Structure
- `data/`: Dataset and loading script
- `src/`: Training script
- `models/`: Trained model
- `dvc.yaml`: Pipeline configuration
- `.github/workflows/`: CI configuration
- `.gitignore`: Ignored files
- `README.md`: Documentation
- `requirements.txt`: Dependencies

## CI
- GitHub Actions runs `dvc repro` on every push to `main`, updating `dvc.lock`.

## Next Steps
- Explore additional models or hyperparameter tuning with MLflow.




