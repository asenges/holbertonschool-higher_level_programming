#!/usr/bin/python3
""" Module Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Object Builder """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ __width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ __width setter """
        self.__width = width

    @property
    def height(self):
        """ __height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ __height setter """
        self.__height = height

    @property
    def x(self):
        """ __x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ __x setter """
        self.__x = x

    @property
    def y(self):
        """ __y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ __y setter """
        self.__y = y
