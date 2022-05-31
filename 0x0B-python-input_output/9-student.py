#!/usr/bin/python3
"""
This module defines a class student
"""


class Student:
    """
    This is the class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        This method builds the object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This method retrieves a dict repr of any
        Student instance
        """
        return self.__dict__
