import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def length(self, other):
        return round(math.hypot((self.x - other.x), (self.y - other.y)), 2)


class PatchedPoint(Point):

    def __init__(self, x = 0, y = 0):
        if isinstance(x, tuple):
            print(x[0], x[1])
            a = x[0]
            b = x[1]
            super().__init__(a, b)
        else:
            super().__init__(x, y)

    
point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

point = PatchedPoint((3, 44))
print(point.x, point.y)

first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
