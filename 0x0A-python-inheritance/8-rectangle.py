#!/usr/bin/python3
"""
kile module inado
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class defined
    """
    def __init__(self, width, height):
        """
        method def
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
