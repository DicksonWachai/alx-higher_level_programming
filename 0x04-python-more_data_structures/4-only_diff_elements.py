#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set_1 - set_2
    set_4 = set_2 - set_1
    set_5 = set_3 | set_4
    return set_5
