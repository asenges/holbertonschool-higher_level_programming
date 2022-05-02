#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list:
        max_n = 0
        for i in my_list:
            if i > max_n:
                max_n = i
        return max_n
    else:
        return None
