#!/usr/bin/python3
"""
mod def
"""


def add_attribute(a_class, att_name, att_value):
    """
    method def
    """
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(a_class, att_name, att_value)
