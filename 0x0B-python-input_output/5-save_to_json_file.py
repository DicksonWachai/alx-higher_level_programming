#!/usr/bin/python3


"""Save Object to file"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to text file
    using JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
