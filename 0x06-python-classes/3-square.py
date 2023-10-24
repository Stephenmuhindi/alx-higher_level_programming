#!/usr/bin/python3
"""this is a square class"""


class Square:
    """defined methodand exceptions"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """defines a square returns the current square area"""
        area = self.__size * self.__size
        return area
