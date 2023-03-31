#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests
if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: \
    {type(res.text)}\n\t- content: {res.text}")
