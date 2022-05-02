#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_v1, a_v2, b_v1, b_v2 = 0, 0, 0, 0

    if len(tuple_a) == 0:
        a_v1 = 0
        a_v2 = 0
    if len(tuple_a) == 1:
        a_v1 = tuple_a[0]
        a_v2 = 0
    if len(tuple_a) > 1:
        a_v1 = tuple_a[0]
        a_v2 = tuple_a[1]
    if len(tuple_b) == 0:
        b_v1 = 0
        b_v2 = 0
    if len(tuple_b) == 1:
        b_v1 = tuple_b[0]
        b_v2 = 0
    if len(tuple_b) > 1:
        b_v1 = tuple_b[0]
        b_v2 = tuple_b[1]

    new_tuple = tuple()
    new_tuple = (a_v1 + b_v1, a_v2 + b_v2)
    return new_tuple
