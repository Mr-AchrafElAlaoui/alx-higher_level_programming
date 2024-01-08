#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Function that replaces an element in a list
    without modifying the original"""
    len_my_list = len(my_list)

    if idx >= len_my_list or idx < 0:
        return None
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
