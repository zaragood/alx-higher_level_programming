#!/usr/bin/python3
"""creating a class "Base"""


class Base:
    """definning a Base class with private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """definning a class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
