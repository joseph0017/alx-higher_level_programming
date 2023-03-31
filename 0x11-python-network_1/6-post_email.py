#!/usr/bin/python3
"""
script that makes a POST request to URL with an email
"""

import requests
from sys import argv

if __name__ == "__main__":
    payload = {'email': argv[2]}
    res = requests.post(argv[1], data=payload)
    print(res.text)
