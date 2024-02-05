#!/usr/bin/python3


"""Import Rectangle module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """defines the instances of square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    """"Calculate area of square"""
    def area(self):
        return self.__size * self.__size

    """"String"""
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
