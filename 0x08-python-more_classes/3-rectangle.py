#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    definition of methods and inst
    """
    def __init__(self, width=0, height=0):
        """
        creates new instances of Rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @property
    def height(self):
        """
        heigh getter
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        gets area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        gets perimeter
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        displaying rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for x in range(self.__height):
            for y in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        # remove blank line
        rectangle.pop()

        return "".join(rectangle)
