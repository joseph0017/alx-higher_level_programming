#!/usr/bin/python3
"Defines a class Square"


class Square:
    """class square with size set to default of 0
    size must be an integer and should not be 
    less than zero"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
