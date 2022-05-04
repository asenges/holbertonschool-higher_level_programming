#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = dict()
    for key, value in a_dictionary.items():
        item = ({key: value * 2})
        new_dict.update(item)
    return new_dict
