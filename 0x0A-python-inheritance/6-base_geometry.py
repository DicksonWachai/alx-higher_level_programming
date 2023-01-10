#!/usr/bin/python3


"""Raise an exception on instance"""


class BaseGeometry:

    """Public instance raises excepetion with message"""
    def area(self):
        raise Exception("area() is not implemented")
