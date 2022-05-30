#!/usr/bin/python3
"""
This module contains a function that checks if
the object is an instance of, or if the object
is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if the object is
    an instance of, or if the object is an instance
    of a class that inherited from, the specified class
    otherwise returns False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
