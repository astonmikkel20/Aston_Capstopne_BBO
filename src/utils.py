import numpy as np

def format_query(point):
    """
    Convert a point like [0.75, 0.72] into:
    0.750000-0.720000
    """
    return "-".join(f"{x:.6f}" for x in point)

def get_best_point(X, y):
    """
    Return:
    - best index
    - best input point
    - best output value
    """
    best_idx = np.argmax(y)
    return best_idx, X[best_idx], y[best_idx]

def get_top_points(X, y, top_n=5):
    """
    Return the top_n best points sorted by output descending.
    """
    idx = np.argsort(y)[::-1][:top_n]
    return idx, X[idx], y[idx]