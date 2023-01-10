#!/usr/bin/python3
"""module for counting characters in a file"""


def write_file(filename="", text=""):
    """Method that returns the number of lines of a text file"""
    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.write(text)
        number_of_characters = len(text) + 5
        myfile.close()
        print(number_of_characters)
