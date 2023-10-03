#!/usr/bin/python3
digit1 = 0

while digit1 < 10:
    digit2 = digit1 + 1

    while digit2 < 10:
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")

        digit2 += 1

    digit1 += 1
