#!/usr/bin/python3

"""Class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Attribute and Method of this class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of this class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of rectangle"""
        return self.__width

    @property
    def height(self):
        """Gets height of rectangle"""
        return self.__height

    @property
    def x(self):
        """Gets the x variable of rectangle"""
        return self.__x

    @property
    def y(self):
        """Gets the y variable of rectangle"""
        return self.__y

    @width.setter
    def width(self, width):
        """Sets the value of width"""
        if (type(width) is not int):
            raise TypeError("Width must be an integer")
        if width <= 0:
            raise ValueError("Width must be greater than 0")

        self.__width = width

    @height.setter
    def height(self, height):
        """Sets the value of height"""
        if (type(height) is not int):
            raise TypeError("Height must be an integer")
        if height <= 0:
            raise ValueError("Height must be greater than 0")

        self.__height = height

    @x.setter
    def x(self, x):
        """Sets the value of x"""
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be greater than 0")

        self.__x = x

    @y.setter
    def y(self, y):
        """Sets the value of y"""
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be greater than 0")

        self.__y = y
