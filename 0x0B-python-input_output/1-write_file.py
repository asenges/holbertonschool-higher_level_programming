#!/usr/bin/python3
"""
This module writes to a file
"""


def write_file(filename="", text=""):
    """
    This function writes to a file
    """
    with open(filename, "w", encoding='utf8') as file:
        return file.write(text)
