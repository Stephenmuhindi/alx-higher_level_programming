#!/usr/bin/python3
"""
definition for task4
"""

def text_indentation(text):
    """
    text indent methods
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    y = 0
    delims = '.?:'

    for x, char in enumerate(text):
        for delim in delims:
            if char is delim:
                y += 1
                text = text[:x + y] + ' ' + text[x + y:]

    list = text.split()

    for word in list:
        if word[-1:] is "." or word[-1:] is "?" or word[-1:] is ":":
            print(word, end="\n\n")
        elif word is list[len(list) - 1]:
            print(word, end="")
        else:
            print(word, end=" ")
