#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as t:
        print("Exception: {}".format(t), file=sys.stderr)
        return None
    else:
        return result
