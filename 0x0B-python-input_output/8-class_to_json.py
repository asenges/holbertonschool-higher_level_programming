#!/usr/bin/python3
"""
This module returns an object dict
"""


def class_to_json(obj):
    """
    This class inherits from obj and returns its dict
    """
    return obj.__dict__
