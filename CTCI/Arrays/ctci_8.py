"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""

import unittest


def zero_element(matrix):
    M = len(matrix)
    N = len(matrix[0])

    i = 0

    zero_column = []

    while i != M:
        if 0 in matrix[i]:
            zero_column += [i for i, x in enumerate(matrix[i]) if x == 0]
            zero_column = list(set(zero_column))
            matrix[i] = N*[0]
        i += 1

    for i in range(M):
        for index in zero_column:
            matrix[i][index] = 0
    return matrix


def zero_matrix_2(matrix):
    m = len(matrix)
    n = len(matrix[0])

    isRowZero = False
    isColTrue = False


    for i in matrix[0]:
        if i == 0:
            isRowZero = True
            break

    for j in range(n):
        if matrix[0][j] == 0:
            isColTrue = True
            break

    print(matrix, isColTrue, isRowZero)

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(m):
        if matrix[0][i] == 0:
            nullifyRow(matrix, i)

    for j in range(n):
        if matrix[j][0] == 0:
            nullifyCol(matrix, j)

    if isRowZero:
        nullifyRow(matrix, 0)

    if isColTrue:
        nullifyCol(matrix, 0)

    return matrix

def nullifyRow(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def nullifyCol(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix_2(test_matrix)
            self.assertEqual(actual, expected)


class TestZeroElement(unittest.TestCase):

    data = [
        ([[1, 2, 3, 0, 5], [1, 2, 3, 4, 5], [1, 0, 3, 4, 5], [1, 0, 3, 4, 5]],
         [[0, 0, 0, 0, 0], [1, 0, 3, 0, 5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    ]

    def test_zero(self):
        for d in self.data:
            result = zero_element(d[0])
            assert result == d[1]

if __name__ == "__main__":
    unittest.main()