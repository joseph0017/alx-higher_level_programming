#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """
    a class Square that defines a square, based on 3-square.py
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) !=2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size < 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

