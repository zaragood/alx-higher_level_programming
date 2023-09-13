#!/usr/bin/python3
"""creating a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """definning a class Rectangle"""

    def __init__(self, width, height):
        """Instantiation with width and height"""

        self.integer_validator('width', width)
        self.integer_validator('heigth', height)
        self.__width = width
        self.__height = height

    def area(self):
        """computes the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns formatted string"""
        a = str(self.__width)
        b = str(self.__height)
        return "[Rectangle]" + " " + a + "/" + b
