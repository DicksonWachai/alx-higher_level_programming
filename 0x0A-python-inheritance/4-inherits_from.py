#!/usr/bin/python3


""""Checks if object inherited from class"""


def inherits_from(obj, a_class):

    """Returns a Boolean if class is inherited"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
