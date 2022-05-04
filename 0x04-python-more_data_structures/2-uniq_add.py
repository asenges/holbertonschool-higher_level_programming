#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    add_set = set(my_list)
    for i in add_set:
        sum += i
    return sum
