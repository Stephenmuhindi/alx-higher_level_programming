#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
from urllib import request, parse


if __name__ == '__main__':
    if len(argv) > 2:
        data = parse.urlencode({'email': argv[2]}).encode('ascii')
        req = request.Request(argv[1], data)
        with request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
