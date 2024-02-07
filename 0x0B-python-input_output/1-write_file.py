#!/usr/bin/python3

""" write to file """


def write_file(filename="", text=""):

    """function writes to file and counts characters"""
    with open(filename, 'w', encoding="utf-8") as f:
        char_count = f.write(text)
    return char_count
