#!/usr/bin/python3
"""
This module appends to a file
"""


def append_write(filename="", text=""):
    """
    This function appends to a file
    """
    with open(filename, "a", encoding='utf8') as file:
        return file.write(text)
