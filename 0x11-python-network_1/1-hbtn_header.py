#!/usr/bin/python3
"""
script that makes a request to and displays X-Request-Id value
"""

import urllib.request
from sys import argv
with urllib.request.urlopen(argv[1]) as response:
   print(f"{response.getheader('X-Request-Id')}")
