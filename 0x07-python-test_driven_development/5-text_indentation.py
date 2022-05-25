#!/usr/bin/python3
""" This module prints a text with 2 new lines after ., ? and :
@text must be a string, otherwise raise a TypeError
There should be no space at the beginning or at the end of each printed line
Return: None
"""


def text_indentation(text):
    """
    Return: None - prints a text
    """
    print_spacing = True
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for i in (text):
            if i == '.' or i == '?' or i == ':':
                print(i.strip())
                print()
                print_spacing = False
            else:
                if print_spacing is False:
                    print_spacing = True
                    continue
                else:
                    print(i, end='')
