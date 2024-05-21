from models import text_preprocessing 

def test_vectorize_text():
    vectorizer = text_preprocessing.CountVectorizer()
    data = ["This is a sample sentence.", "This is another one."]
    vectorized_data = vectorizer.fit_transform(data)
    
    assert vectorized_data.shape[1] == len(vectorizer.get_feature_names_out())  

test_vectorize_text()
