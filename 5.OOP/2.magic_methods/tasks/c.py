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

    def __add__(self, other):
        o = PatchedPoint(other)
        lhs = PatchedPoint(self.x, self.y)
        lhs.x = lhs.x + o.x
        lhs.y = lhs.y + o.y
        return lhs

    def __iadd__(self, other):
        o = PatchedPoint(other)
        self.x += o.x
        self.y += o.y
        return self


point = PatchedPoint(44, 44)
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)

first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
