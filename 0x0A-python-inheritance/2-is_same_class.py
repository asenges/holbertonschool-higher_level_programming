#!/usr/bin/python3
"""
This module contains a function that checks
if the object is exactly an instance of the
specified class
"""


def is_same_class(obj, a_class):
    """
    This function returns True if the object is
    exactly an instance of the specified class
    otherwise returns False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
