#!/usr/bin/python3
"""
This module reads a file
"""


def read_file(filename=""):
    """
    This function reads a file
    """
    with open(filename, encoding='utf8') as file:
        print(file.read(), end="")
