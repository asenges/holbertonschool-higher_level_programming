#!/usr/bin/python3
"""
This module implements a class that inherits from list
"""


class MyList(list):
    """
    This class inherits from class List
    """
    def print_sorted(self):
        """
        This method prints a sorted list
        """
        print(sorted(self))
