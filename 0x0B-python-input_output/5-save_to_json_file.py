#!/usr/bin/python3
"""
mod def
"""
import json


def save_to_json_file(my_obj, filename):
    """
    method def
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
