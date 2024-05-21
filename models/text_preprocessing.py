from sklearn.feature_extraction.text import CountVectorizer

def vectorize_text(text_data):
    vectorizer = CountVectorizer()
    vectorized_data = vectorizer.fit_transform(text_data)
    return vectorized_data, vectorizer
