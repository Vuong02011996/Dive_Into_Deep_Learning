import numpy as np
import math


def transpose():
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(matrix)
    print("\n")
    print(np.transpose(matrix))
    print(matrix.T)


if __name__ == '__main__':
    transpose()