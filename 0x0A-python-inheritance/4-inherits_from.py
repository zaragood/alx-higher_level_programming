#!/urs/bin/python3
"""definning a method 'inherits_from'"""


def inherits_from(obj, a_class):
    """ function that returns True if the object
    is an instance of a class that inherited"""
    return issubclass(type(obj), a_class) and a_class != type(obj)
