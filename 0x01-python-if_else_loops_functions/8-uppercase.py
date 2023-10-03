#!/usr/bin/python3
def uppercase(s):
    uppercase_str = ''.join([chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c for c in s])
    print("{}".format(uppercase_str))
