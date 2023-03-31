#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        search_query = {"q": argv[1]}
    else:
        search_query = {"q": ""}

    res = requests.post('http://0.0.0.0:5000/search_user', data=search_query)
    json_object = res.json()
    try:
        if json_object:
            print(f"[{json_object.get('id')}] {json_object.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
