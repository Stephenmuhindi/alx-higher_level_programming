#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for q in range(0, x):
        try:
            print("{}".format(my_list[q]), end="")
            count += 1
        except IndexError:
            pass
    print()
    return count
