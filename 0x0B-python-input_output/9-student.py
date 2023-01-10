#!/usr/bin/python3
"""Module or file for class student"""


class Student:
    """a Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a copy of dictionary"""
        return self.__dict__.copy()
