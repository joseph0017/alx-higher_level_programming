#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """
    a class Square that defines a square, based on 3-square.py
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return(self.__size)
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return(self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()