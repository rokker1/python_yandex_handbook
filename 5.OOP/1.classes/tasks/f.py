class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = min(point1[0], point2[0]), max(point1[1], point2[1])
        self.point2 = max(point1[0], point2[0]), min(point1[1], point2[1])
        self.x = abs((self.point1[0] - self.point2[0]))
        self.y = abs(self.point1[1] - self.point2[1])

    def perimeter(self):
        return round(2 * (self.x + self.y), 2)

    def area(self):
        return round(self.x * self.y, 2)

    def get_pos(self):
        return round(self.point1[0], 2), round(self.point1[1], 2)

    def get_size(self):
        return round(self.x, 2), round(self.y, 2)

    def move(self, dx, dy):
        self.point1 = (self.point1[0] + dx, self.point1[1] + dy)
        self.point2 = (self.point2[0] + dx, self.point2[1] + dy)

    def resize(self, width, height):
        self.x = width
        self.y = height
        self.point2 = (self.point1[0] + width, self.point1[1] + height)

# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.get_pos(), rect.get_size())
# rect.move(1.32, -5)
# print(rect.get_pos(), rect.get_size())


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
