#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # get a list of the key-value pairs of the dictionary
    items = list(a_dictionary.items())
    # sort the items
    items.sort()
    # iterate over the key-value pairs
    for key, value in items:
        print("{}: {}".format(key, value))
