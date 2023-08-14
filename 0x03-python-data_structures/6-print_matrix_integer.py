#!/usr/bin/python3

# function that prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            for item in row:
                print("{:d}".format(item), end=" ")
            print()
