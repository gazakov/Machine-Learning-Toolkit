from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from logger_config import setup_logger

logger = setup_logger()  

def train_random_forest(X_train, y_train, n_estimators=100, random_state=42):
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    model.fit(X_train, y_train)
    return model

def evaluate_random_forest(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

def train(data):
    logger.info("Training random forest model...")
    model = RandomForestClassifier().fit(data)
    logger.info("Model trained successfully.")
    return model
