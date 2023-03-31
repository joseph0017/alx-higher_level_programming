#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    response = requests.get(
        'https://api.github.com/user',
        auth= HTTPBasicAuth(argv[1], argv[2]),
    )
    get_id = response.json().get("id")
    print(get_id)
