import numpy as np


def rotate(m, angle):
    k = angle // 90
    n = np.rot90(m, -k)
    return n


print(rotate(np.arange(12).reshape(3, 4), 90))
print(rotate(np.arange(12).reshape(3, 4), 270))

