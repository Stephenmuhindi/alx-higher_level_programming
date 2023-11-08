#!/usr/bin/python3
"""
mod def
"""


class BaseGeometry:
    """
    Base Geometry class
    """

    def area(self):
        """
        Method not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validator
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size):
        """
        Initialize a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square
        """
        return self._Rectangle__width ** 2
