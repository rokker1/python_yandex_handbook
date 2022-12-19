import math

class Rectangle:

    def __init__(self, point1, point2):
        self.set(point1, point2)

    def set(self, p1, p2):
        self.point1 = min(p1[0], p2[0]), max(p1[1], p2[1])
        self.point2 = max(p1[0], p2[0]), min(p1[1], p2[1])
        self.x = abs(self.point1[0] - self.point2[0])
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

    def rotate_point(self, point, anchor, angle):
        angle = angle / 360 * 2 * math.pi
        new_x = (point[0] - anchor[0]) * math.cos(angle) - (point[1] - anchor[1]) * math.sin(angle) + anchor[0]
        new_y = (point[0] - anchor[0]) * math.sin(angle) + (point[1] - anchor[1])  * math.cos(angle) + anchor[1]
        return new_x, new_y

    def get_center(self):
        cx = (self.point1[0] + self.point2[0]) / 2
        cy = (self.point1[1] + self.point2[1]) / 2
        return cx, cy

    def turn(self, angle=90):
        c = self.get_center()
        p1 = self.rotate_point(self.point1, c, angle)
        p2 = self.rotate_point(self.point2, c, angle)
        self.set(p1, p2)

    def scale(self, factor):
        c = self.get_center()
        alpha = math.atan(self.y / self.x)
        scale = math.sqrt(((self.point1[0] - c[0]) ** 2) + ((self.point1[1] - c[1]) ** 2)) / 2
        p1 = (
            self.point1[0] - factor * math.cos(alpha) * scale,
            self.point1[1] + factor * math.sin(alpha) * scale
        )
        p2 = (
            self.point2[0] + factor * math.cos(alpha) * scale,
            self.point2[1] - factor * math.sin(alpha) * scale
        )
        self.set(p1, p2)



rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size())
rect.scale(2.0)
print(rect.get_pos(), rect.get_size())

