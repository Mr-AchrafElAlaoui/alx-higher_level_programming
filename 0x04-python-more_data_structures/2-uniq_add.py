#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Function that adds all unique integers in a list"""

    return sum(integer for integer in set(my_list))
