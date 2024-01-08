#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds 2 tuples"""
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)

    if len_tuple_a < 2:
        tuple_a += (0,) * (2 - len_tuple_a)
    else:
        tuple_a = tuple_a[:2]

    if len_tuple_b < 2:
        tuple_b += (0,) * (2 - len_tuple_b)
    else:
        tuple_b = tuple_b[:2]

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
