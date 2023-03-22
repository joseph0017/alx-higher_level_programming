#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """a class Square that defines the size:
    -Private Instance attribute is size
    -Instantiation with size (no type/value verification)"""
    def __init__(self, size):
        self.__size = size
