#!/usr/bin/python3
"""
mod def
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class inst
    """

    def __init__(self, size):
        """
        init methd
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        area def
        """
        return self.__size ** 2

    def __str__(self):
        """
        strdefined
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
