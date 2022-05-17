#!/usr/bin/python3
""" 4. Access and update private attribute """


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

    @property
    def size(self):
        """ __size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """ __size setter """
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """ square area l^2 """
        return self.__size * self.__size
