#!/usr/bin/python3


"""Define a class square that takes an attribute size"""


class Square:
    """Instatiate class with a private attribute"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    """Access the position"""
    @property
    def position(self):
        return self.__position

    """Mutate the position"""
    @position.setter
    def position(self, value):
        for i in range(len(position)):
            if position[i] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """"Calclulate the area of square"""
    def area(self):
        return self.__size ** 2

    """"Print # as per size"""
    def my_print(self):
        if self.__size == 0:
            print()
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
