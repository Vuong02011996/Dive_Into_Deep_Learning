import numpy as np
import math
from numpy import mat, shape
from numpy import array
from scipy.linalg import lu

"""
https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html
"""


def transpose():
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(matrix)
    print("\n")
    print(np.transpose(matrix))
    print(matrix.T)


def linear_equation():
    a = array([[2., 1., -1.], [-3., -1., 2.], [-2., 1., 2.]])
    b = array([-8., 11., 3.])
    c = np.linalg.solve(a, b)
    print(c)


# Gauss Jordan Elimination
def gauss_elimination():
    a = array([[2., 4., 4., 4.], [1., 2., 3., 3.], [1., 2., 2., 2.], [1., 4., 3., 4.]])
    a = array([[2., 1., -1.], [-3., -1., 2.], [-2., 1., 2.]])
    b = array([-8., 11., 3.])
    u = lu(a, permute_l=True)

    print(u[1])



if __name__ == '__main__':
    # transpose()
    gauss_elimination()