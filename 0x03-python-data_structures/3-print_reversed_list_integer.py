#!/usr/bin/python3

# function that prints all integers of a list, in reverse order

def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list[::-1]
    for item in reversed_list:
        print("{}".format(item))
