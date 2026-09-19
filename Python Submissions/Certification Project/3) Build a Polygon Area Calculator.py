import math

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.height * self.width

    def get_perimeter(self) -> int:
        return 2 * (self.height + self.width)

    def get_diagonal(self) -> float:
        return math.sqrt((self.width ** 2) + (self.height ** 2))

    def get_picture(self) -> str:
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        picture = ''
        for i in range(self.height):
            picture += '*' * self.width + "\n"
        return picture

    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_amount_inside(self, rectangle):
        return self.get_area() // rectangle.get_area()

class Square(Rectangle):
    def __init__(self, side: int) -> None:
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f'Square(side={self.height})'

    def set_side(self, side: int) -> None:
        self.set_height(side)

    def set_height(self, side):
        self.height = side
        self.width = side

    def set_width(self, side):
        self.width = side
        self.height = side


