import numpy as np


def multiplication_matrix(N):
    matrix = np.array([multiplier * np.arange(1, N + 1) for multiplier in range(1, N + 1)])
    return matrix


print(multiplication_matrix(10))