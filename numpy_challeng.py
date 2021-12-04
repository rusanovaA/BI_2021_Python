import numpy as np
from numpy.linalg import multi_dot


def matrix_multiplication(matrix_1, matrix_2):
    print(np.matmul(n, m))


def multiplication_check(matrix_list):
    try:
        multi_dot(matrix_list)
        return True
    except Exception:
        return False


def multiply_matrices(matrix_list):
    try:
        res = multi_dot(matrix_list)
        return res
    except Exception:
        print('None')


def compute_2d_distance(point1, point2):
    if len(point1) == 2 and len(point2) == 2:
        print(np.linalg.norm(point1 - point2))
    else:
        print('Try another coordinates')


def compute_multidimensional_distance(point1, point2):
    print(np.linalg.norm(point1 - point2))

def compute_pair_distances(array):
    new_array = array.reshape(array.shape[0], 1, array.shape[1])
    res = np.sqrt(np.einsum('ijk, ijk->ij', array - new_array, array - new_array))
    return res
