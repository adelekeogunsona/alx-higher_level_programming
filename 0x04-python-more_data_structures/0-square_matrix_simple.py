#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
    return new_list
