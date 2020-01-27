#!/usr/bin/python3
"""
this module define the Base class
"""


import json


class Base:
    """this is the Base class avoids duplicate code"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return a json string representation
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"
