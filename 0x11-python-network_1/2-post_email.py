#!/usr/bin/python3
"""
script that makes a POST request to URL with an email
"""

import urllib.request
from sys import argv
if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        
        r = urllib.requests.post('https://httpbin.org/post', data={'email': argv[2]})
        print(f"Your email is: {getattr(argv[2])}")
