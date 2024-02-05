#!/usr/bin/python3


"""Module has a function that indents text"""


def text_indentation(text):
    """ This function indents text
    It takes one argument
    Args: text
    Prints two new lines after '.', '?', ':'

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char in ".?:":
            print(char, end="\n\n")
        else:
            print(char, end="")
