#!/usr/bin/python3
""" 2. Size validation """


class Square:
    """ class Square """
    def __init__(self, size=0):
        """ constructor method """
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
