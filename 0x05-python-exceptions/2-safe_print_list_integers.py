#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    c = 0
    for e in range(0, x):
        try:
            print("{:d}".format(my_list[e]), end="")
             += 1
        except (ValueError, TypeError):
            print("", end="")
    print()
    return c
