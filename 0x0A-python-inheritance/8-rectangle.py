#!/usr/bin/python3


"""ïmport module from 7-base_geometry.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Defines a class Rectangle inherits BaseGeometry"""


class Rectangle(BaseGeometry):

    """"definitions of instances"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
