#!/usr/bin/python3
"""
This module writes to a file
"""


def append_write(filename="", text=""):
    """
    This function writes to a file
    """
    with open(filename, "a", encoding='utf8') as file:
        return file.write(text)
