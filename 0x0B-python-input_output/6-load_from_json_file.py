#!/usr/bin/python3
"""
This module creates an object
from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    This function creates an object from  a JSON file
    """
    with open(filename, "r", encoding="utf8") as file:
        return json.load(file)
