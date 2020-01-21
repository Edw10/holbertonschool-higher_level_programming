#!/usr/bin/python3
"""
this module define a function to know if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """ this fucntion return true if obj is part of a_class"""
    return isinstance(obj, a_class)
