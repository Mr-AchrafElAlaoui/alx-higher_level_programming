#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: [integer ** 2
                    for integer in row], matrix))
