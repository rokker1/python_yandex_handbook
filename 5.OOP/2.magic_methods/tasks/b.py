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

    def __init__(self, x=0, y=0):
        if isinstance(x, tuple):
            a = x[0]
            b = x[1]
            super().__init__(a, b)
        else:
            super().__init__(x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"


point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))

first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))