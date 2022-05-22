#!/usr/bin/python3
""" This module prints a square with the character #
@size must be an integer, otherwise raise a TypeError
if size is less than 0, raise a ValueError
Return: None
"""


def print_square(size):
    """
    Return: None - prints a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
