#!/usr/bin/python3
"""
This module returns an object representation
from a given JSON
"""


import json


def from_json_string(my_str):
    """
    This function returns a JSON object
    """
    return json.loads(my_str)
