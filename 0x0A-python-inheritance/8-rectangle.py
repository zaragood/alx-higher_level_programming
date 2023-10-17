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
