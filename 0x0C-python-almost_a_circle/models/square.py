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
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """updates attributes from arguments"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
