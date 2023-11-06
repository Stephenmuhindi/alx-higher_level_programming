#!/usr/bin/python3

class MyList(list):
    """Class with method instance"""
    pass

    def print_sorted(self):
        """method"""

        print(sorted(list(self)))
