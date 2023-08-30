#!/usr/bin/python3

"""defines a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializing a class attributes

        Args:
            size (int): size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """getter methode for atribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for 'size' attribute."""

        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")

            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)
