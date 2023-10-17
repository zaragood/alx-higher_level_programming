#!/usr/bin/python3
"""Defines a function print_square"""


def print_square(size):
    """
    function that prints a square with the character #

        Args:
            @size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
    print()
