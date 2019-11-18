#to modify

import numpy as np

def load_data():
    n = 10

    data = np.random.random((1000,512))
    labels = np.random.randint(n, size=(1000, 1))
    
    test_data = np.random.random((100,512))
    test_labels = np.random.randint(n, size=(100, 1))

    return data, labels, test_data, test_labels