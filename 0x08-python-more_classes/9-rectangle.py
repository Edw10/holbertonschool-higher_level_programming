#!/usr/bin/python3
"""
this module define a rectangle empty class
"""


class Rectangle():
    """
    rectangle class
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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
        a = (str(self.print_symbol)*self.__width)
        return (str(self.print_symbol)*self.__width+'\n')*(self.__height-1)+a

    def __repr__(self):
        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        a = rect_1.area()
        a1 = rect_2.area()
        if a >= a1:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        return cls(size, size)
