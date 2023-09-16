#!/usr/bin/python3
"""importing the Base classs"""
from models.base import Base

"""creating a class 'Rectangle'"""


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor
         Initializing a class attribute with height and width
         x, y and id

        Args:
            @width (int): width of rectangle
            @Height (int): height of the rectangle
            @x (int)
            @y (int)
        """
        super().__init__(id)
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getting the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the attribute width"""
        self.__width = width

    @property
    def height(self):
        """getting the private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """sets the attribute of height"""
        self.__height = height

    @property
    def x(self):
        """getting the private instance attribute x"""
        return (self.__x)

    @height.setter
    def x(self, x):
        """sets the attribute of x"""
        self.__x = x

    @property
    def y(self):
        """getting the private instance attribute y"""
        return (self.__height)

    @y.setter
    def y(self, y):
        """sets the attribute of y"""
        self.__y = y
