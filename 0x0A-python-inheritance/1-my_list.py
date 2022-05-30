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
        for i in self:
            if not isinstance(i, int):
                raise TypeError("must be a list of integers")
        print(sorted(self))
