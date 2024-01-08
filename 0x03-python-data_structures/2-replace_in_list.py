#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Function that replaces an element of a list at a specific position"""
    len_my_list = len(my_list)

    if idx < 0 or idx >= len_my_list:
        return my_list

    else:
        my_list[idx] = element
        return my_list
