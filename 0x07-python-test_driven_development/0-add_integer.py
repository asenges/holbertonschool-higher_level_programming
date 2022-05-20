#!/usr/bin/python3
""" This module returns the addition of two integers:
@a and @b must be integers or floats, otherwise raise a TypeError 
@a and @b must be first casted to integers if they are float
Return: integer - the addition of a and b
"""


def add_integer(a, b=98):
    """ 
    Return: additionof two integers.  
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
