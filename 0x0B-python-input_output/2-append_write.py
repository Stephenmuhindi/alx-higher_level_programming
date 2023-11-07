#!/usr/bin/python3
"""
mod def
"""


def append_write(filename="", text=""):
    """
    method func
    """
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
    return num
