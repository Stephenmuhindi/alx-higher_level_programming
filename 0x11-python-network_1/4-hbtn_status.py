#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
response must be display(tabulation before -)
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    text = requests.get(url).text
    rtr_str = 'Body response:\n\t- type: {}\n\t- content: {}'
    print(rtr_str.format(type(text), text))
