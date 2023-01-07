import numpy as np

M, N = (int(x) for x in input().split())

def snake(M, N, direction="H"):
    size_ = M * N
    row_index = 0
    if direction == "H":
        a = np.arange(1, size_ + 1, dtype="int16").reshape(N, M)
        
        
        for row in a:
            if row_index % 2 == 1:
                a[row_index] = row[::-1]
            row_index += 1

    if direction == 'V':
        a = np.arange(1, size_ + 1, dtype="int16").reshape(M, N)
        for row in a:
            if row_index % 2 == 0:
                a[row_index] = row[::-1]
            row_index += 1
        a = np.rot90(a, k=1)
    return a


print(snake(5, 3))
print(snake(5, 3, direction='V'))