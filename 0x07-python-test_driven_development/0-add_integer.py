#!/usr/bin/python3
"""defines a function that add_integer"""


def add_integer(a, b=98):
    """
    function that returns the addition of two integers

        Args:
             @a (int, float): first integer
             @b (int, float): second integer

        Returns:
            result a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
