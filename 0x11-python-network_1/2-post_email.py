#!/usr/bin/python3
""" 
script that makes a request to and displays X-Request-Id value
"""

import urllib.request
from sys import argv
with urllib.request.urlopen(argv[1]) as response:
    r = urllib.requests.post('https://httpbin.org/post', data={'email': argv[2]})
    print(f"Your email is: {getattr(argv[2])}")
