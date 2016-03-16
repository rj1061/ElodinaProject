from sklearn.feature_extraction import DictVectorizer

class featureExtractor:

    def __init__(self):
        self.vec = DictVectorizer()

    def vectorize_this(flat_json):
        return vec.fit_transform(flat_json).toarray()
        
    def vectorized_names(flat_json):
        return vec.get_feature_names()
