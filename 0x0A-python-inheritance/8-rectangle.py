#!/usr/bin/python3
"""
This module contains an class Rectangle
that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a class Rectangle
    """
    def __init__(self, width, height):
        """
        This is the Constructor method of Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
