#!/usr/bin/python3

"""First class: Base"""


class Base:
    """Attributes and methods of this class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
