#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width property of class Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height property of class Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x property of class Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y property of class Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        public method area that returns
        the area value of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        public method that prints in stdout
        the Rectangle instance with the character #
        """
        print('\n' * self.y + '\n'.join([' ' * self.x +
                                         '#' * self.width
                                         for i in range(self.height)]))

    def __str__(self):
        """
        Prints string representation of a Rectangle
        """
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Public method that assigns an argument
        to each attribute
        """
        attributes = ["id", "width", "height", "x", "y"]
        for atrr, arg in zip(attributes, args):
            setattr(self, atrr, arg)
        for atrr, arg in kwargs.items():
            setattr(self, atrr, arg)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
