#!/usr/bim/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index in range(len(row)):
            if index != len(row) - 1:
                print("{}".format(row[index]), end=" ")
            else:
                print("{}".format(row[index]), end="")
        print()
