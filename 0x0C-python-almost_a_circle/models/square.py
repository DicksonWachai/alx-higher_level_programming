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
