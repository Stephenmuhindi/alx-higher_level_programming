#!/usr/bin/python3
"""
module def
"""


class Student:
    """
    student def
    """
    def __init__(self, first_name, last_name, age):
        """
        init func def
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        defines a student
        """
        final_list = {}
        all_string = True
        if type(attrs) is not list:
            all_string = False

        if type(attrs) is list:
            for i in attrs:
                if type(i) != str:
                    all_string = False
        if not all_string:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    final_list[i] = self.__dict__[i]
            return final_list
