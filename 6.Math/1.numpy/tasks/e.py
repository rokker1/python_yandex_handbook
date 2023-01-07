import math

x1, y1 = (float(x) for x in input().split())
r2, f2 = (float(x) for x in input().split())
x2, y2 = r2 * math.cos(f2), r2 * math.sin(f2)
print(x1, y1, x2, y2)
distance = math.dist((x1, y1), (x2, y2))
print(distance)