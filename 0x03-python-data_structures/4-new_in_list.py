#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Function that replaces an element in a list
    without modifying the original"""
    len_my_list = len(my_list)

    if idx < 0 or idx >= len_my_list:
        return None

    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
