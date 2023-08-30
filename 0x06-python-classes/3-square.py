#!/usr/bin/python3

"""defines a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializing a class attributes

        Args:
            size (int): size of the square.
        """
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)
