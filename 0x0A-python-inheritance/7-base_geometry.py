#!/usr/bin/python3


"""Defines class BaseGeometry"""


class BaseGeometry:
    """"Defines instances of class"""
    def area(self):
        """"raises exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
