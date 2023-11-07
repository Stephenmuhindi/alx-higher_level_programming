#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
module func def
"""


class Rectangle(BaseGeometry):
    """
    base geomerty def
    """

    def __init__(self, width, height):
        """
        initializing method
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        area def
        """
        return self.__width * self.__height

    def __str__(self):
        """
        str methd
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
