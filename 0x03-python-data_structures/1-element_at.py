#!/usr/bin/python3
def element_at(my_list, idx):
    length_list = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > length_list:
        return None
    else:
        return my_list[idx]
