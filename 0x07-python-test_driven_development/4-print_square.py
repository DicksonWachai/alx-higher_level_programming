#!/usr/bin/python3


"""Module prints a square with the character #"""


def print_square(size):
    """Defines the function print_square

    The function takes one argument

    Args: size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif ((isinstance(size, float)) and size < 0):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
