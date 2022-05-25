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
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        line = ""
        for i in range(len(text)):
            if text[i] in ['.', ':', '?']:
                line += text[i]
                print(line.strip())
                print()
                line = ""
            else:
                line += text[i]
        print(line.strip(), end="")
