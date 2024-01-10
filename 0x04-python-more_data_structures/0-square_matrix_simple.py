#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Function that computes the square value of all int of matrix"""
    new_matrix = list(map(lambda row: [integer ** 2
                          for integer in row], matrix))
    return new_matrix
