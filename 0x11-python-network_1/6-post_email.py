#!/usr/bin/python3
"""
email as a parameter,
displays the body of the response
"""
from sys import argv
import requests


if __name__ == '__main__':
    print(requests.post(argv[1], data={'email': argv[2]}).text)
