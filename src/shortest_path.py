import networkx as nx
import numpy as np

from utils.matrixutils import adjacency_dense, boolean_matrix_mult, is_complete_graph


def min_plus_apsp(graph):
    """
    All-pairs shortest paths using the min-plus product algorithm.
    :param graph:
    :return:
    """
    pass


def seidel(A):
    """
    Recursive form of Seidel's algorithm for all-pairs shortest path in a connected graph with
    undirected and unweighted edges.
    :param A: Adjacency matrix
    :return:
    """
    if is_complete_graph(A):
        return A
    else:
        A_sq_bool = boolean_matrix_mult(A, A)
        A_prime = np.logical_or(A_sq_bool, A).astype(int)
        np.fill_diagonal(A_prime, 0)
        D = seidel(A_prime)
        DA = D @ A
        R = np.zeros(A.shape, dtype=int)
        # TODO: remove explicit loop
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                deg_j = A[j, :].sum()
                R[i][j] = 2 * D[i][j] - 1 if DA[i][j] < deg_j * D[i][j] else 2 * D[i][j]

        return R
