#!/usr/bin/python3


"""Creates class Rectangle"""


class Rectangle:
    """Initialize class attribute"""
    number_of_instances = 0
    print_symbol = '#'

    """Defines the instances of Rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        Rectangle.number_of_instances += 1

    """Defines the width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Defines the height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Calculate the area of rectangle"""
    def area(self):
        return self.__width * self.__height

    """Calculate the perimeter of rectangle"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            result = (2 * self.__height) + (2 * self.__width)
            return result

    """Print out str"""
    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            if i != self.__height - 1:
                string = string + str(self.print_symbol) * self.__width + "\n"
            else:
                string = string + str(self.print_symbol) * self.__width
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    """Deletes an instance"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """Defines a static method"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height
        if area_1 > area_2:
            return rect_1
        elif area_2 > area_1:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(height=size, width=size)
