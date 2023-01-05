import numpy as np


def make_board(N):
    if N <= 0:
        return np.array([], dtype='uint8')
    number = (N // 2 + (N % 2))
    temp = [number * [(multiplier % 2), ((multiplier + 1) % 2)] for multiplier in range(1, N + 1)]
    matrix = np.array(temp, dtype='uint8')
    return matrix[:N, :N]


print(make_board(16))