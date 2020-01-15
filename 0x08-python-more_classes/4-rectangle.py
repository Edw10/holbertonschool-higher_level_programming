#!/usr/bin/python3
"""
this module define a rectangle empty class
"""


class Rectangle():
    """
    rectangle class
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width*2) + (self.__height*2)

    def __str__(self):
        if self.__width is 0 or self.__height is 0:
            return ''
        return ("#"*self.__width + "\n")*(self.__height - 1)+("#"*self.__width)

    def __repr__(self):
        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"
