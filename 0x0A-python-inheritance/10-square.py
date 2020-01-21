#!/usr/bin/python3
"""
this module define the empty class base_geometry
"""


class BaseGeometry():
    """ this class is a base for the geometry forms"""
    def __init__(self):
        pass

    def area(self):
        pass

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """ this class is a rectangle inherit by base_geometry """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return('[Rectangle] ' + str(self.__width) + '/\
' + str(self.__height))

    def area(self):
        return self.__width * self.__height


class Square(Rectangle):
    """ this class is a square that inherit from Rectangle """
    def __init__(self, size):
        super().__init__(size, size)
