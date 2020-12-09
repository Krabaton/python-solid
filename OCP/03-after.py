from math import pi


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return self.radius ** 2 * pi


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        sum = 0
        for el in self.shapes:
            sum += el.area_of()
        return sum


fig_1 = Rectangle(10, 10)
fig_2 = Rectangle(4, 5)
fig_3 = Rectangle(3, 3)
fig_4 = Circle(7)
fig_5 = Circle(10)
area = AreaCalculator([fig_1, fig_2, fig_3, fig_4, fig_5])
print(area.total_area())
