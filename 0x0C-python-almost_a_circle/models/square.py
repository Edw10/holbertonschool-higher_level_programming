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
                ' - ' + str(self.width)
