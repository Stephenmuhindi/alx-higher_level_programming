#!/usr/bin/python3
"""
func decrptn
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    shape
    """

    def __init__(self, width, height):
        """
        creates one rect
        height
        width
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
