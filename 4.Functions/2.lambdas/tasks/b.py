def make_matrix(size, value=0):
    if isinstance(size, int):
        w = h = size
    elif isinstance(size, tuple):
        w = size[0]
        h = size[1]
    return [[value for j in range(w)] for i in range(h)]


print(make_matrix(2, 333))
print(make_matrix((4, 2), 333))
