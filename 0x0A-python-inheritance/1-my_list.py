#!/usr/bin/python3
"""
this module define the mylist class
"""


class MyList(list):
    """ this class define a list """

    def print_sorted(self):
        a = self.copy()
        a.sort()
        print(a)
