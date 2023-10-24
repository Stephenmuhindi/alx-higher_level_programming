#!/usr/bin/python3
"""this is a square class"""


class Square:
    """defined methodand exceptions"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size > 0:
            for a in range(self.__position[1]):
                print()
            for b in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
