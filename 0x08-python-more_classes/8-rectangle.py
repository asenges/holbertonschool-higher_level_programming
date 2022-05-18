#!/usr/bin/python3
""" This is the module documentation """


class Rectangle:
    """ This is the class documentation """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter  """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif not value >= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ width getter  """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif not value >= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ returns rectangle area A=w*h """
        return self.__width * self.__height

    def perimeter(self):
        """ returns rectangle perimeter P=2(h+w) """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """ str """
        str_rep = ""
        if self.__width == 0 or self.__height == 0:
            return str_rep
        for i in range(0, self.__height):
            for i in range(0, self.__width):
                str_rep += str(self.print_symbol)
            if i is not self.__height - 1:
                str_rep += "\n"
        return str_rep

    def __repr__(self):
        """ repr """
        return (type(self).__name__ + "(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    def __del__(self):
        """ del """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ cmp rectangles  """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_2) > Rectangle.area(rect_1):
            return rect_2
        else:
            return rect_1
