#!/usr/bin/python3
"""Module for Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter property for the size"""
        return self.width

    @size.setter
    def size(self, value):
        """getter property for the size value"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation for class Square"""
        return(
            f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        """
        public method that assigns attributes:

        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        attributes = ["id", "size", "x", "y"]
        for attr, arg in zip(attributes, args):
            setattr(self, attr, arg)
        for attr, arg in kwargs.items():
            setattr(self, attr, arg)

    def to_dictionary(self):
        attributes = ["id", "x", "size", "y"]
        return {key: getattr(self, key) for key in attributes}
