#!/usr/bin/python3
"""defines an empty class"""


class Rectangle:
    """represents a class object 'Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing a class attribute with height and width

        Args:
            @width (int): width of rectangle
            @Height (int): height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """getting the private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the attribute of width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting the private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the attribute of height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width +  self.__height)
