#!/usr/bin/python3
"""creating an empty class"""


class BaseGeometry:
    """An empty class BaseGeometry"""

    def area(self):
        """Public instance method: def area(self):
        that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method: integer_validator"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
             raise ValueError(name + " must be greater than 0")
