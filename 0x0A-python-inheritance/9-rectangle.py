#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
func def
"""


class Rectangle(BaseGeometry):
    """
    classdef
    """
    def __init__(self, width, height):
        """
        Method
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Method2
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
