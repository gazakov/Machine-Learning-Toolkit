import pandas as pd
import sys
sys.path.append('/home/ushad/Documents/Project') 
from models.your_model import train_model, evaluate_model

def test_vectorize_text():
    vectorizer = CountVectorizer()
    data = ["This is a sample sentence.", "This is another one."]
    vectorized_data = vectorizer.fit_transform(data)

    assert vectorized_data.shape[1] == len(vectorizer.get_feature_names_out())

def test_your_model(): 

    test_data = pd.DataFrame({
      'feature1': [1, 2, 3],
      'feature2': [4, 5, 6],
      'target': [0, 1, 0]
    })

    X = test_data[['feature1', 'feature2']]
    y = test_data['target']

    model = train_model(X, y)
    assert model is not None


    evaluate_model(model, X, y)
