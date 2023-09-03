#!/usr/bin/python3
"""defines a matrix_divided"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix and return a new matrix

        Args:
            @matrix (int): matrix must be a list of lists of integers or floats
            @div (int): div must be a number

        Return:
            Returns a new matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix.copy()))

