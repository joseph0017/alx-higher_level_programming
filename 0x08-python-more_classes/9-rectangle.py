#!/usr/bin/python3
"""
Defines a class rectangle
"""


class Rectangle:
    """Definition of a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constructor for the Rectangle class"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """deletes an instance of class object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """getter property for the width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """setter property for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif(value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter property for the height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """setter property for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif(value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height or self.__width == 0:
            self.perimeter = 0
        return(2 * (self.__width + self.__height))

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1.area()
    
    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance
        with width == height == size
        """
        return cls(size, size)
