#!/usr/bin/python3
"""
this module define the empty class base_geometry
"""


class BaseGeometry():
    """ this class is a base for the geometry forms"""
    def area(self):
        raise Exception('area() is not implemented')
