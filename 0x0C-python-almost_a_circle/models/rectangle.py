#!/usr/bin/python3
"""
this is the module that define the rectangle class
"""


from base import Base


class Rectangle(Base):
    """this is the rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value

    def validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(name + ' must be >= 0')
        else:
            if value <= 0:
                raise ValueError(name + ' must be > 0')

    def area(self):
        return (self.width * self.height)

    def display(self):
        print("\n"*self.y, end='')
        print((" "*self.x + "#"*self.width + '\n')*(self.height), end='')

    def __str__(self):
        return ('[Rectangle] (' + str(self.id) + ') ' +
                str(self.x) + '/' + str(self.y) +
                ' - ' + str(self.width) + '/' + str(self.height))

    def update(self, *args, **kwargs):
        if args is not None:
            i = 0
            for args in args:
                if i == 0:
                    self.id = args
                if i == 1:
                    self.width = args
                if i == 2:
                    self.height = args
                if i == 3:
                    self.x = args
                if i == 4:
                    self.y = args
                i += 1
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

