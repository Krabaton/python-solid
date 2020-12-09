
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        sum = 0
        for el in self.shapes:
            sum += el.width * el.height
        return sum


fig_1 = Rectangle(10, 10)
fig_2 = Rectangle(4, 5)
fig_3 = Rectangle(3, 3)
area = AreaCalculator([fig_1, fig_2, fig_3])
print(area.total_area())
