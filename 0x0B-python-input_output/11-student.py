#!/usr/bin/python3
"""
mod def
"""


class Student:
    """
    mod def
    """
    def __init__(self, first_name, last_name, age):
        """
        init method def
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        iteration thru arg
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

    def reload_from_json(self, json):
        """
        reloads
        """
        for i in json:
            self.__dict__[i] = json[i]
