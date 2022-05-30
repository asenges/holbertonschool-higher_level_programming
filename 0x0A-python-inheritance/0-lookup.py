#!/usr/bin/python3
"""
This module contains function that returns
the list of available attributes and methods
of an object
"""


def lookup(obj):
    """
    This function returns the list of available
    attributes and methids of an object
    """
    return(dir(obj))
