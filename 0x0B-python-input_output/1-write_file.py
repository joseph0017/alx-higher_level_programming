#!/usr/bin/python3
"""module for counting characters in a file"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, encoding="utf-8") as my_file_0:
        data = my_file_0.read()
        number_of_characters = len(data)
        print(number_of_characters)
