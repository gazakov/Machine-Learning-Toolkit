from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from joblib import load
import pandas as pd


def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

def split_data(data, target_column, test_size=0.2):
    y = data[target_column]
    X = data.drop(columns=[target_column])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cf_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy: ', accuracy)
    print('Confusion Matrix: ', cf_matrix)

if __name__ == "__main__":
    data = load_data('/path/to/processed/data.csv')  # update this
    X_train, X_test, y_train, y_test = split_data(data, 'target_column')  # update 'target_column'
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

def predict_with_model(new_data):
    # Load your trained model
    model = load('model.joblib')

    # Preprocess your new data using the same steps as your training data
    preprocessed_data = preprocess_new_data(new_data)
    
    # Create predictions
    predictions = model.predict(preprocessed_data)
    
    return predictions