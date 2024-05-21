import argparse
import pandas as pd
from src.models import your_model
from logger_config import setup_logger

logger = setup_logger(__name__)

def main(data_path, target_column):
    data = pd.read_csv(data_path)
    X_train, X_test, y_train, y_test = your_model.split_data(data, target_column)
    model = your_model.train_model(X_train, y_train)
    model.save('model.joblib')  # Save the trained model to a file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train a machine learning model.')
    parser.add_argument('data_path', type=str, help='Path to the CSV file with the training data.')
    parser.add_argument('target_column', type=str, help='Name of the target column in the dataset.')
    args = parser.parse_args()
    main(args.data_path, args.target_column)
