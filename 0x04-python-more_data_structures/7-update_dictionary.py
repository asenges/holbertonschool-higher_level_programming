#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    item = {key: value}
    a_dictionary.update(item)
    return a_dictionary
