#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """represents a class Square"""

    def __init__(self, size=0):
        """initializing a private attribute 'size'

        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")

        else:
            self.__size = size

        if size < 0:
            raise ValueError("size must be >= 0")
