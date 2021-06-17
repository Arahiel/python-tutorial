from module2.decorators import log_all

value = "Static value"

@log_all
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive!")
        else:
            self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive!")
        else:
            self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def message(self, text):
        print(text)

    def __str__(self) -> str:
        return "Rectangle: width: {0}, height: {1}".format(self.width, self.height)

    def __repr__(self) -> str:
        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Rectangle) and self.width == other.width and self.height == other.height

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented