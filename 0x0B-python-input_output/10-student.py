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

    def to_json(self, attrs=None):
        """
        This method retrieves a dict repr of any
        Student instance
        """
        obj = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
            for k in set(self.__dict__.keys()) & set(attrs):
                obj.setdefault(k, self.__dict__.get(k))
            return obj
        return self.__dict__
