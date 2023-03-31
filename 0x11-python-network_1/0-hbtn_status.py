#!/usr/bin/python3
"""
script that makes a fetch request to https://intranet.hbtn.io/status
"""

import urllib.request
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        request = response.read()
        print(f"Body response:\n\t- type: {type(request)}\n\t- \
        content: {request} \n\t- utf8 content: {request.decode('utf-8')}")
