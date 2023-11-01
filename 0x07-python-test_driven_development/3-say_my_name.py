#!/usr/bin/python3
"""
task 2
"""


def say_my_name(first_name, last_name=""):
    """methods for above"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
