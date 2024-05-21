import argparse
import pandas as pd
from joblib import load
from src.models import your_model

def main(data_path, target_column):
    data = pd.read_csv(data_path)
    _, X_test, _, y_test = your_model.split_data(data, target_column)
    model = load('model.joblib')  # Load the trained model from a file
    your_model.evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate a trained machine learning model.')
    parser.add_argument('data_path', type=str, help='Path to the CSV file with the test data.')
    parser.add_argument('target_column', type=str, help='Name of the target column in the dataset.')
    args = parser.parse_args()
    main(args.data_path, args)
