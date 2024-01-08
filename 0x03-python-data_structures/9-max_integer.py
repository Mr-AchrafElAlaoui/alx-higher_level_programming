#!/usr/bin/python3

def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list"""
    if not my_list:
        return None
    else:
        my_list.sort(reverse=True)
        return my_list
