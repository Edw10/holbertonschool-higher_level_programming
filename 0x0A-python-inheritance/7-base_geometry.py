#!/usr/bin/python3
"""
this module define the empty class base_geometry
"""


class BaseGeometry():
    """ this class is a base for the geometry forms"""
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name +' must be an integer')
        if value <= 0:
            raise ValueError(name +' must be greater than 0')
