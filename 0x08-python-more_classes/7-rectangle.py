#!/usr/bin/python3
"""
Defines a class rectangle
"""


class Rectangle:
    """Definition of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle AKA constructor"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """deletes an instance from the class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        
    @property
    def width(self):
        """getter for the width property"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """setter for the width property"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        """getter for the height property"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """setter for the height property"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif(value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """method that returns the rectangle area"""
        return(self.__width * self.__height)

    def perimeter(self):
        """method that returns the rectangle perimeter"""
        if self.__height or self.__width == 0:
            self.perimeter = 0
        return(self.__width * 2  + self.__height * 2)

    def __str__(self):
        """custom string representation as #"""
        string = ""
        if self.__width and self.__height == 0:
            print("")
        else:
            string = "\n".join(str(self.print_symbol) * self.__width
                               for h in range(self.__height))
        return string

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance
        """
        return "Rectangle ({:d}, {:d})".format(self.__width, self.__height)
