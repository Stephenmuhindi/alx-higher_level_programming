#!/usr/bin/python3
"""
locked class def
"""


class LockedClass:
    """
    methods and instances
    """
    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = "first_name"
