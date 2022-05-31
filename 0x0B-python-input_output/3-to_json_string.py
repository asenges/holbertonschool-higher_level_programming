#!/usr/bin/python3
"""
This module returns a JSON representation
of a given object
"""


import json


def to_json_string(my_obj):
    """
    This function returns a JSON object
    """
    return json.dumps(my_obj)
