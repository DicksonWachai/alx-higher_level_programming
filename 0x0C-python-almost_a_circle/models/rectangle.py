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

    def area(self):
        """Calculates area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints out rectangle with # """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns an informal string representation"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args):
        """Assign arguments to class attributes"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
