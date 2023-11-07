#!/usr/bin/python3
"""
mod def
"""


def write_file(filename="", text=""):
    """
    method def
    """
    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
    return num
