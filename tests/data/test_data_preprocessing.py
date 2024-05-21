from sklearn.feature_extraction.text import CountVectorizer
import unittest

class TestDataPreprocessing(unittest.TestCase):
    def test_vectorize_text(self):
        vectorizer = CountVectorizer()
        data = ["This is a sample sentence.", "This is another one."]
        vectorized_data = vectorizer.fit_transform(data)
        
        self.assertEqual(vectorized_data.shape[1], len(vectorizer.get_feature_names_out()))

if __name__ == '__main__':
    unittest.main()
