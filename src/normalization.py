from sklearn import preprocessing
import numpy as np

class normalization:

    def __init__(self):

    def normalize(flat_json_vector):
        x = np.array(flat_json_vector)
        x_scaled = preprocessing.scale(x)

        return preprocessing.normalize(x_scaled)
