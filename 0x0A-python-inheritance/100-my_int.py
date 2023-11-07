#!/usr/bin/python3
"""
Mod def
"""


class MyInt(int):
    """
    int def
    """

    def __eq__(self, other):
        """
        equal
        """
        return self.real != other

    def __ne__(self, other):
        """
        not equal
        """
        return self.real == other
