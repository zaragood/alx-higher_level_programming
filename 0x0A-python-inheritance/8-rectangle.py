#!/usr/bin/python3
"""creating an class BaseGeometry"""


class BaseGeometry:
    """definning a class BaseGeometry"""

    def area(self):
        """Public instance method: def area(self):
        that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:integer_validator"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


"""creating a class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """definning a class Rectangle"""

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('heigth', height)
        self.__width = width
        self.__height = height
