from enum import Enum

'''

private
protected
public

'''

class SideType(Enum):
    TYPE_WIDTH = 'width'
    TYPE_HEIGHT = 'height'


class Shape:
    def area_of(self):
        pass


class WidthfulShape:
    def set_width(self, width):
        pass


class HeightfulShape:
    def set_height(self, height):
        pass


class Rectangle(Shape, WidthfulShape, HeightfulShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_side(self, size, side):
        if SideType.TYPE_WIDTH == side:
            self.width = size
        if SideType.TYPE_HEIGHT == side:
            self.height = size

    def set_width(self, width):
        self.set_side(width, SideType.TYPE_WIDTH)

    def set_height(self, height):
        self.set_side(height, SideType.TYPE_HEIGHT)

    def area_of(self):
        return self.width * self.height


class Square(Shape, WidthfulShape):
    def __init__(self, size):
        self.edge = size

    def set_side(self, size):
        self.edge = size

    def set_width(self, width):
        self.set_side(width)

    def area_of(self):
        return self.edge ** 2


square = Square(20)
print(square.area_of())
rect = Rectangle(5, 10)
print(rect.area_of())


def test_shape_size(figure):
    figure.set_width(10)
    figure.set_height(20)
    return figure.area_of() == 200


# print(test_shape_size(square))
print(test_shape_size(rect))
