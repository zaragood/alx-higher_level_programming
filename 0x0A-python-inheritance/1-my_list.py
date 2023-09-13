#!/usr/bin/python3
"""creating a class MyList"""

class MyList(list):
    def print_sorted(self):
        print(sorted(self))
        return sorted(self)
