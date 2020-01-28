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
        if cls.__name__ is "Rectangle":
            file_w = open("Rectangle.json", "w")
        elif cls.__name__ is "Square":
            file_w = open("Square.json", "w")
        js_list = []
        if list_objs:
            for obj in list_objs:
                js_list.append(obj.to_dictionary())
        file_w.write(cls.to_json_string(js_list))
        file_w.close()

    @staticmethod
    def from_json_string(json_string):
        """
        return the list represented by the string
        """
        if json_string:
            return json.loads(json_string)
        return ([])

    @classmethod
    def create(cls, **dictionary):
        """
        create the object with the dictionary attributes
        """
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        return a list of objects
        """
        file_r = open(cls.__name__ + '.json', "r")
        l_dict = cls.from_json_string(file_r.read())
        l_obj = []
        for dicty in l_dict:
            l_obj.append(cls.create(**dicty))
        return l_obj
