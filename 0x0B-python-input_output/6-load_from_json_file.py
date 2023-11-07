#!/usr/bin/python3
"""
mod def
"""
import json


def load_from_json_file(filename):
    """
    method def
    """
    with open(filename, "r") as f:
        return json.loads(f.readline())
