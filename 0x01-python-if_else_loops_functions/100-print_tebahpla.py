#!/usr/bin/python3
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    char = chr(c).lower() if i == 0 else chr(c).upper()
    print("{}".format(char), end="")
    i = 32 if i == 0 else 0
