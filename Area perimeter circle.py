class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.1415926535 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.1415926535 * self.radius
radius = float(input())
circle = Circle(radius)
print(circle.area())
print(circle.perimeter())