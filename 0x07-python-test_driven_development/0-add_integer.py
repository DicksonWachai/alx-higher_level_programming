#!/usr/bin/python3

"""Function does a sum of integers and floats"""


def add_integer(a, b=98):
    """defines the functionality"""
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
