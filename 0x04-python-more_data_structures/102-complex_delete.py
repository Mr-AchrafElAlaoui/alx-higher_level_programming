#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Function that deletes keys with a specific value in a dictionary"""
    keys_to_delete = [key for key, dic_value in
                      a_dictionary.items() if dic_value == value]
    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
