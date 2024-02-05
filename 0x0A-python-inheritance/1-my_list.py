#!/usr/bin/python3"


"""Prints a list from my class"""


class MyList(list):

    """"Defines a list inherited and sorted in ascending order"""
    def print_sorted(self):
        print(sorted(self))
