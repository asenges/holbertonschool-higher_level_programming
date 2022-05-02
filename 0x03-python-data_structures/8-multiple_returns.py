#!/usr/bin/python3

def multiple_returns(sentence):
    new_tuple = tuple()
    f_ch = ""
    strlen = len(sentence)

    if sentence == "":
        f_ch = None
    else:
        f_ch = sentence[0]

    new_tuple = (strlen, f_ch)
    return new_tuple
