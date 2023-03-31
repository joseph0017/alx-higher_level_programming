#!/usr/bin/python3
"""
script that makes a request to a URL
if not successful, displays an errorcode
"""

from sys import argv

import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        request = response.read()
        try:
            request
        except urllib.error.HTTPError as err:
            print(f"Error code: {err.code}")
