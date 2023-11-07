#!/usr/bin/python3


def read_file(filename=""):
    """
    scans texts then putchars it
    """

    with open(filename) as f:
        text = f.read()
        print(text, end="")
