#!/usr/bin/python3
"""
Python script that lists commits by someone
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    response = requests.get(url)
    json_obj = response.json()
    num_commits = 0
    for i in json_obj:
        if num_commits < 10:
            print("{}: {}".format(i.get("sha"),
                  i.get("commit").get("author").get("name")))
        num_commits += 1
