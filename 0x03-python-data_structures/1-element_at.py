#!/usr/bin/python3

def element_at(my_list, idx):
    """Function that retrieves an element from a list"""
    len_my_list = len(my_list)
    if idx < 0 or idx >= len_my_list:
        return None
    else:
        return my_list[idx]
