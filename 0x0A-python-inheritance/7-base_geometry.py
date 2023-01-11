#!/usr/bin/python3


""""Raises Exceptions on the Class BaseGeometry"""


class BaseGeometry:

    def area(self):

        """"Create exception with message"""
        raise Exception("area() is not implemented")

    """"Instance that validates the value"""
    def integer_validator(self, name, value):

        """Raise TypeError if value is not integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        """Raise ValueError is value is less or equal 0"""
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
