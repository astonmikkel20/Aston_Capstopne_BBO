import numpy as np

def load_function(inputs_path, outputs_path):

    X = np.load(inputs_path)
    y = np.load(outputs_path)
    return X, y