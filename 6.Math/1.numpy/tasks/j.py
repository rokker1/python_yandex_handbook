import numpy as np


def stairs(vec):
    a = np.array([np.roll(vec, x) for x in range(vec.size)])
    return a


print(stairs(np.arange(3)))

