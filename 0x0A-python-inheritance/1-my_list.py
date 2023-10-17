#!/usr/bin/python3
"""module to creating a class MyList"""


class MyList(list):
    """creating a class MyList"""
    def print_sorted(self):
        print(sorted(self))
        return sorted(self)
