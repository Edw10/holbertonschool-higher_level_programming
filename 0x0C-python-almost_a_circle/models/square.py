#!/usr/bin/python3
"""
this module define the square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this is the square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """this initialice a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this is the str representation"""
        return ('[Square] (' + str(self.id) + ') ' +
                str(self.x) + '/' + str(self.y) +
                ' - ' + str(self.width))

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

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
                    self.height = args
                if i == 2:
                    self.x = args
                if i == 3:
                    self.y = args
                i += 1
