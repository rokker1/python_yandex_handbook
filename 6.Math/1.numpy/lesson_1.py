import numpy as np

a = np.array([9, 8, 7])
b = np.array([1, 2, 3])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# matrix multiplication
c = np.array([[11, 2, 1],
              [4, 5, 60],
              [7, 8, 9]])
d = np.array([[1, 0, 1],
              [0, 1, 0],
              [1, 0, 1]])
print(c @ d)
print(c.dot(d))
print(c)

# transposing and rotation
e = np.arange(1, 13).reshape(4, 3)
print("e=", e)
print("transponing")
print(e.transpose())
print("left rotation")
print(np.rot90(e, -1))
print("right rotation")
print(np.rot90(e))

# sum/min/max
print(c)
print("max in c is:", np.max(c, axis=0))
print("min in c is:", np.min(c, axis=0))
print("sum of c is:", np.sum(c, axis=1))

d = np.arange(16, 129, 8).reshape(5, -1)
print(d)
print()
e = d[1:-1, 1:-1]
print(e, e.shape)

for row in d:
    print(row)

print()
print("; ".join(str(el) for el in d.flat))

from time import time
t = time()
print(f"Результат итератора: {sum(x ** 0.5 for x in range(2  * 10 ** 8))}.")
print(f"{time() - t} с.")
t = time()
print(f"Результат numpy: {np.sqrt(np.arange(2 * 10 ** 8)).sum()}.")
print(f"{time() - t} с.")
