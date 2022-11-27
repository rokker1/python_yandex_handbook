N = int(input())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Check(self, another_point):
        if self.x // 10 == another_point.x // 10 and self.y // 10 == another_point.y // 10:
            return True
        else:
            return False

    def __eq__(self, __o: object) -> bool:
        return __o.x == self.x and __o.y == self.y

    def __hash__(self):
        return hash(139 * self.x + 37 * self.x)


points = []
matrix = {}
for i in range(N):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    points.append(Point(x, y))

for i in range(len(points) - 2):
    count = 0
    for j in range(i + 1, len(points)):
        if points[i].Check(points[j]) and points[i] != points[j]:
            count += 1
    matrix[i] = count

print(max(matrix.values()) + 1)
