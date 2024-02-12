#!/usr/bin/python3


"""The square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Methods and attributes of the class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the class"""
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Informal string representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.size}"

    @property
    def size(self):
        """Gets the value of the size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        self.__width = value
        self.__height = value
