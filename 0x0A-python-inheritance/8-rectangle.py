#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
rectangle sumbufu
"""


class Rectangle(BaseGeometry):
    """
    Rectangle def
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
