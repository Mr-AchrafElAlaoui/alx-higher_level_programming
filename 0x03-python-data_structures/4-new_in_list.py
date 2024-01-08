#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Function that replaces an element in a list
    without modifying the original"""

    if idx >= len(my_list) or idx < 0:
        return None
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
