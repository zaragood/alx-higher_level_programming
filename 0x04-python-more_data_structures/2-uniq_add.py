#!/usr/bin/python3

#  function that adds all unique integers in a list

def uniq_add(my_list=[]):

    unique_list = []
    sum_list = 0

    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    for item in unique_list:
        sum_list += item
    return (sum_list)
