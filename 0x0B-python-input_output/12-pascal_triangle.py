#!/usr/bin/python3
"""
This module  returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers
    """
    obj = list()
    tmp = list()
    for i in range(n):
        aux = list()
        a = -1
        b = 0
        for j in range(len(tmp) + 1):
            if a == -1 or b == len(tmp):
                aux += [1]
            else:
                aux += [tmp[a] + tmp[b]]
            a += 1
            b += 1
        obj.append(aux)
        tmp = aux[:]
    return obj
