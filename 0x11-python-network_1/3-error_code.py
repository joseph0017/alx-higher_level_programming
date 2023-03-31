#!/usr/bin/python3
"""
script that makes a request to a URL
if not successful, displays an errorcode
"""
from sys import argv
import urllib.request
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf8'))
    except error.HTTPError as err:
            print('Error code: {}'.format(err.code))
