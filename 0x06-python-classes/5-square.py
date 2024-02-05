#!/usr/bin/python3


"""Define a class square that takes an attribute size"""


class Square:
    """Instatiate class with a private attribute"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Access the field using getters"""
    @property
    def size(self):
        return self.__size

    """Mutate the field using setter"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """"Calclulate the area of square"""
    def area(self):
        return self.__size * self.__size

    """"Print # as per size"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
