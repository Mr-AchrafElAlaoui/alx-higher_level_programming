#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers"""
    for row in matrix:
        for idx, integer in enumerate(row):
            if idx == len(row) - 1:
                print("{:d}".format(integer), end="")
            else:
                print("{:d}".format(integer), end=" ")
        print()
    if not matrix:
        print()
