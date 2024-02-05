#!/usr/bin/python3


"""Define a class square that takes an attribute size"""


class Square:
    """Instatiate class with a private attribute"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """Define an instance that calculates area"""
    def area(self):
        return self.__size * self.__size
