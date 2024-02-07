#!/usr/bin/python3


"""JSON string to Object"""

import json


def from_json_string(my_str):
    """function returns an object from json string"""
    return json.loads(my_str)
