#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers of a list , in reverse ordes"""
    my_list.reverse()

    for item in my_list:
        print("{}".format(item))
