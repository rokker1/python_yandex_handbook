class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def perimeter(self):
        return round(2 * (abs(self.point1[0] - self.point2[0]) + 
            abs(self.point1[1] - self.point2[1])), 2)

    def area(self):
        return round(abs((self.point1[0] - self.point2[0]) * 
            (self.point1[1] - self.point2[1])), 2)

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

