#!/usr/bin/python3
""" This module creates a class: Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherites from Reactangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """calls the super class instances"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return formated string for square"""
        a = str(self.id)
        b = str(self.x)
        c = str(self.y)
        d = str(self.width)
        return f"[Square] ({a}) {b}/{c} - {d}"

    @property
    def size(self):
        """getting the size"""
        return self.width

    @size.setter
    def size(self, size):
        """setting size attribute"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """adding args and kwargs
        Args:
            *args (ints): New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        arguments = ['id', 'size', 'x', 'y']

        if args:
            for i, arg_name in enumerate(arguments):
                if i < len(args):
                    setattr(self, arg_name, args[i])
        else:
            for key, value in kwargs.items():
                if key  in arguments:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representation of Squ"""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.width,
                "y": self.y
                }
