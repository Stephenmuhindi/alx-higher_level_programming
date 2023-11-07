#!/usr/bin/python3
"""
mod def
"""


def pascal_triangle(n):
    """
    method def
    """
    final_list = []
    if n <= 0:
        return final_list
    for x in range(1, n+1):
        new_row = []
        num = 1
        for y in range(1, x+1):
            new_row.append(num)
            num = num * (x - y) // y
        final_list.append(new_row)
    return final_list
