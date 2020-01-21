#!/usr/bin/python3
"""
this module define a function to know if an object is an instance of a class
"""


def inherits_from(obj, a_class):
    """ this fucntion return true if obj is part of a_class"""
    if issubclass(obj.__class__, a_class) and obj.__class__ is not a_class:
        return True
