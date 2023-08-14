#!/usr/bin/python3

# Function that retrieves an element from a list
def element_at(my_list, idx):
    list_len = len(my_list)
    for item in my_list:
        if idx < 0:
            return (item)
        elif idx > list_len - 1:
            return (None)
        else:
            return(my_list[idx])
