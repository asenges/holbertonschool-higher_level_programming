#!/usr/bin/python3
"""
This module implements a class that inherits from list
"""


class MyList(list):
    """
    This class inherits from list
    """
    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))
