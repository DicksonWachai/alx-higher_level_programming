#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = ' '.join(str(elem) for elem in row)
        print('{}'.format(row_str))
