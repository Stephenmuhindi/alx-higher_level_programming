#!/usr/bin/python3
"""rectangle """


class Rectangle:
    """
    Class that defines properties
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        methods
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):

        return self.__width

    @property
    def height(self):

        return self.__height

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):

        return self.__height * self.__width

    def perimeter(self):

        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):

        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for x in range(self.__height):
            for y in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):

        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
