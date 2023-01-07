import math

a, b = (int(x) for x in input().split())
if b > a:
    print(1, 1)
else:
    n = math.comb(a, b)
    m = int(n * b / a)
    print(m, n)