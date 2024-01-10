#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    list_set = set(my_list)
    uniq_list = list(list_set)
    for i in uniq_list:
        result = result + i
    return result
