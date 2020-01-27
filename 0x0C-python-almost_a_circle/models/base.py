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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save to a file the json representation
        """
        if list_objs:
            if cls.__name__ is "Rectangle":
                file_w = open("Rectangle.json", "w")
            elif cls.__name__ is "Square":
                file_w = open("Square.json", "w")
            js_list=[]
            for obj in list_objs:
                js_list.append(obj.to_dictionary())
            file_w.write(cls.to_json_string(js_list))
