#!/usr/bin/python3
"""
this is the module that define the rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    this is the rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init a rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        self.validator("y", value)
        self.__y = value

    def validator(self, name, value):
        """
        validator for values
        """
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(name + ' must be >= 0')
        else:
            if value <= 0:
                raise ValueError(name + ' must be > 0')

    def area(self):
        """
        return area
        """
        return (self.width * self.height)

    def display(self):
        """
        display the rectangle with #
        """
        print("\n"*self.y, end='')
        print((" "*self.x + "#"*self.width + '\n')*(self.height), end='')

    def __str__(self):
        """
        str representation
        """
        return ('[Rectangle] (' + str(self.id) + ') ' +
                str(self.x) + '/' + str(self.y) +
                ' - ' + str(self.width) + '/' + str(self.height))

    def update(self, *args, **kwargs):
        """
        update the attributes
        """
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
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        return a dictionary representation
        """
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
