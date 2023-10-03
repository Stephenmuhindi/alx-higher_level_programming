#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return "{}".format(c)
    if c > b:
        return "{}{}".format(a, b)
    return "{}{}".format(a * b, c)
