#!/usr/bin/python3
""" 6. Coordinates of a square """


class Square:
    """ class Square """
    def __init__(self, size=0, pos=(0, 0)):
        """ constructor method """
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

        if not isinstance(pos[0], int) or not isinstance(pos[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(pos, type((int, int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = pos

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

    @property
    def position(self):
        """ __position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """ __position setter  """
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value, type((int, int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ square area l^2 """
        return self.__size * self.__size

    def my_print(self):
        """ print square """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for i in range(0, self.__position[0]):
                    print(" ", end="")
                for i in range(0, self.__size):
                    print("#", end="")
                print()
