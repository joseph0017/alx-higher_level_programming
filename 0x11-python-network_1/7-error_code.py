#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the result
"""

import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    if(res.status_code >= 400):
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
