rle = [('a', 2), ('b', 3), ('c', 1)]
result = "".join([e[0] * e[1] for e in rle])
print(result)