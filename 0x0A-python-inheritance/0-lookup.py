#!/usr/bin/python3
"""Returns lists of attributes available in an object"""


def lookup(obj):

    """Create a variable called attribute for directory lookup"""
    attributes = dir(obj)
    return attributes
