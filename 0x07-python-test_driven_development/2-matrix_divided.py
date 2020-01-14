#!/usr/bin/python3
"""


this module define the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    this function divided all the elements on a matrix by div
    """

    if type(matrix) is not list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
        )
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')

    l_r = len(matrix[0])
    matrix1 = []
    for row in matrix:
        list1 = []
        if type(row) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats'
            )
        if len(row) is not l_r:
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(
                    'matrix must be a matrix (list of lists) \
of integers/floats'
                )
            list1.append(round(float(element)/float(div), 2))
        matrix1.append(list1)
    return matrix1
