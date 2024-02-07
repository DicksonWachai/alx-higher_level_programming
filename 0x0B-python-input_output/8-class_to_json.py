#!/usr/bin/python3


"""Class to JSON"""

import json


def class_to_json(obj):
    """function that returns the dictionary description for
    JSON serialization of an object"""
    encoder = json.JSONEncoder()
    return encoder.encode(obj.__dict__)
