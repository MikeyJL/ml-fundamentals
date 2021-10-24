import numpy as np

def slr_slope_coef (x, y):
    x = np.array(x)
    y = np.array(y)
    x_bar = sum(x) / len(x)
    y_bar = sum(y) / len(y)
    numerator = sum([(x[i] - x_bar) * (y[i] - y_bar) for i in range(len(x))])
    denominator = sum([(x[i] - x_bar) ** 2 for i in range(len(x))])
    return numerator / denominator