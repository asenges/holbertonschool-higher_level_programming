#!/usr/bin/python3
"""
This module writes an object to a file
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This function writes a JSON to a file
    """
    with open(filename, "w", encoding="utf8") as file:
        file.write(json.dumps(my_obj))
