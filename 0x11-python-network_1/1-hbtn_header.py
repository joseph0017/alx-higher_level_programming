#!/usr/bin/python3
"""
script that makes a request and displays X-Request-Id value
"""

import urllib.request
from sys import argv
if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(f"{response.getheader('X-Request-Id')}")
