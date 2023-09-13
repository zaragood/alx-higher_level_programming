#!/usr/bin/python3
"""creating a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """definning a class square"""

    def __init__(self, size):
        """Instantiation with size"""

        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """computes the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        """returns formatted string"""
        b = str(self.__size)
        return "[Square]" + " " + b + "/" + b
