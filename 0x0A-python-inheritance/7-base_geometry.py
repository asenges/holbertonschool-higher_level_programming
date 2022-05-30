#!/usr/bin/python3
"""
This module contains an class BaseGeometry
with an empty method
"""


class BaseGeometry:
    """
    This is a class BaseGeometry
    """
    def area(self):
        """
        This method only raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates if value is an integer
        or if it is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
