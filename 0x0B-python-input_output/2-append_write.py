#!/usr/bin/python3

"""Append to file"""


def append_write(filename="", text=""):
    """function appends and counts characters written"""
    with open(filename, 'a', encoding="utf-8") as f:
        char_count = f.write(text)
    return char_count
