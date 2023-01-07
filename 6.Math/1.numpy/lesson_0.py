import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(f"a[0] = {a[0]}")
print(f"b[0] = {b[0]}")

#number of axis
print(a.ndim)
print(b.ndim)

#shape
print(a.shape)
print(b.shape)

print(a.size)
print(b.size)

print(a.dtype)
print(b.dtype)

print(a.itemsize)
print(b.itemsize)

c = np.array([1, 2, 3], dtype="uint8")
c[0] = 256
print(c)


d = np.array([1, 2.5, 3])
print(d)
print(d.dtype)

e = np.array(['text', 1, 2.5])
print(e)
print(e.dtype)

f = np.zeros((4, 3))
print(f)
print()
g = np.zeros((4, 3), dtype="int32")
print(g)

h = np.arange(1, 10)
print(h)
print()
i = np.arange(1, 5, 0.4)
print(i)

j = np.linspace(1, 5, 10)
print(j)
print(j.ndim)
print(j.dtype)
print(j.size)
print(j.itemsize)

k = np.zeros((4, 3), dtype="uint8")
print(k)
print()
k = k.reshape((2, 6))
print(k)

l = np.ones((4, 3), dtype="uint8")
print(l)
print()
l.resize((2, 2, 3))
print(l)