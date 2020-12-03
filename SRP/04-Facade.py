'''
Фасад — шаблон проектирования, при котором сложная логика скрывается за вызовом более простого API.
Фасад обеспечивает простое общение со сложной частью системы, беря ответственность за настройку
и вызов специфических методов конкретных объектов на себя.
'''

from math import pi
from enum import Enum


class ShapeType(Enum):
    CIRCLE = 'circle'
    SQUARE = 'square'


class Square:
    def __init__(self, length):
        self.length = length

    def area_of(self):
        return self.length ** 2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return pi * (self.radius ** 2)


class Shape:
    def __init__(self, size):
        self.square = Square(size)
        self.circle = Circle(size)

    def area_of(self, figure):
        dict_figure = {
            ShapeType.CIRCLE: self.circle.area_of(),
            ShapeType.SQUARE: self.square.area_of()
        }
        return dict_figure.get(figure, 0)


shape = Shape(42)

print(shape.area_of(ShapeType.CIRCLE))
print(shape.area_of(ShapeType.SQUARE))
print(shape.area_of('ellipse'))

