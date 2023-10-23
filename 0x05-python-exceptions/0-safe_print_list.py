#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret = 0
    while x > 0:
        try:
            print("{}".format(my_list[ret]), end=" ")
            ret += 1
            x -= 1
        except (IndexError, ValueError, TypeError):
            pass
        except Exception:
            print("Catch all")
    print()
    return ret
