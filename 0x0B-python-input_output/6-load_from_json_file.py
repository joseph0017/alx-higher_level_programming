#!/usr/bin/python3
"""Function for load_from_json_file"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="utf-8") as load_file:
        return json.load(load_file)
