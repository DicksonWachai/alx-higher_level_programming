#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_str = '\n'.join([' '.join(str(x) for x in row) for row in matrix])
    print('{}'.format(row_str))
