#!/usr/bin/python3
"""
mod def
"""


class Student:
    """
    class intance def
    """
    def __init__(self, first_name, last_name, age):
        """
        init method def
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        method def
        """
        return self.__dict__
