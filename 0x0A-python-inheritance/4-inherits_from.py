#!/usr/bin/python3
"""
This module contains a function that checks if
the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object is
    an instance of, or if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class, otherwise returns False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
