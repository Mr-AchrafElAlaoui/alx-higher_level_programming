#!/usr/bin/python3

def delete_at(my_list, idx=0):
    """Function that deletes the item at a specific position in a list"""
    len_my_list = len(my_list)

    if len_my_list < 0 or len_my_list >= idx:
        return my_list
    else:
        del my_list[idx]
        return my_list
