#!/usr/bin/python3
"""Module for Base class"""
import json


class Base:
    """Base class for other classes in this module"""
    __nb_objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or not len(list_dictionaries):
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the
        JSON string representation of list_objs to a file
        """
        name_of_file = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [myobj.to_dictionary() for myobj in list_objs]
            with open(name_of_file, "w") as outfile:
                outfile.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the
        list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        cls.__name__ == "Rectangle"
        new_dum = cls(1, 17, 9, 21)
        new_dum.update()
        return new_dum
