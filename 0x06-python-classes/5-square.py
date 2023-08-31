#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """Initializing a class attributes

        Args:
            size (int): size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """getting the privat instance attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of the size attribute"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """calculates the area of a square

        Returns:
            int: the area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
