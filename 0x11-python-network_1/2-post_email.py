#!/usr/bin/python3
"""
script that makes a POST request to URL with an email
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
