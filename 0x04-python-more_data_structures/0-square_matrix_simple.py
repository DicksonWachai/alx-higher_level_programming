#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [[elem**2 for elem in row] for row in matrix]
    return square_matrix
