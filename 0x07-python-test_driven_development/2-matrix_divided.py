#!/usr/bin/python3
""" This module returns a divided matrix of integers or floats:
@matrix must be integers or floats, otherwise raise a TypeError
@div must integers or floats, otherwise raise a TypeError
Return: new_matrix - first matrix divided by div
"""


def matrix_divided(matrix, div):
    """
    Return: divided matrix.
    """
    div_number_msg = "div must be a number"
    div_zero_msg = "division by zero"
    matrix_list_msg = ("matrix must be a matrix "
                       "(list of lists) of integers/floats")
    row_size_msg = ("Each row of the matrix must have "
                    "the same size")

    if ((type(div) is not int and type(div) is not float)
            or type(div) is None or type(div) is bool):
        raise TypeError(div_number_msg)
    if div == 0:
        raise ZeroDivisionError(div_zero_msg)
    if not isinstance(matrix, list):
        raise TypeError(matrix_list_msg)

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError(row_size_msg)
        if not isinstance(i, list):
            raise TypeError(matrix_list_msg)
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(matrix_list_msg)

    new_matrix = list()
    for i in matrix:
        new_list = list()
        for j in i:
            new_list.append(round(j / div, 2))
        new_matrix.append(new_list)
        del(new_list)
    return(new_matrix)
