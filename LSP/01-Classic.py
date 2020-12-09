class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area_of(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height


square = Square(10)
rect = Rectangle(5, 10)


def test_shape_size(figure):
    figure.set_width(10)
    figure.set_height(20)
    return figure.area_of() == 200


print(test_shape_size(square))
print(test_shape_size(rect))

'''
предусловия не могут быть усилены в подклассе
постусловия не могут быть ослаблены в подклассе
'''