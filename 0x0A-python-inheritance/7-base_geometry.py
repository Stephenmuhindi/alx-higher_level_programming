#!/usr/bin/python3
"""
funcdef
"""


class BaseGeometry:
    """class yenyewe"""

    def area(self):
        """
        area def
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validatr mthd
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
