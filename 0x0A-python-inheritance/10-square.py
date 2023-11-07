#!/usr/bin/python3
"""
mod def
"""
Rectangle = __import__('9-rectangle').Rectangle
"""
import def
"""


class Square(Rectangle):
    """
    kile square yafanya
    """

    def __init__(self, size):
        """
        init lives here
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        area def
        """
        return self.__size ** 2
