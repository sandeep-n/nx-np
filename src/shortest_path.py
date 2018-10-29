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


def seidel_wiki(A, n):
    """

    :param A:
    :param n:
    :return:
    """
    if all(A[i][j] for i in range(n) for j in range(n) if i != j):
        return A
    else:
        Z = A @ A
        B = np.matrix(
            [1 if i != j and (A[i][j] == 1 or Z[i][j] > 0) else 0 for j in range(n)] for i in range(n)
        )
        T = seidel_wiki(B, n)
        X = T * A
        degree = [sum(A[i][j] for j in range(n)) for i in range(n)]
        D = np.matrix([
            [2 * T[i][j] if X[i][j] >= T[i][j] * degree[j] else 2 * T[i][j] - 1 for j in range(n)] for i in range(n)
        ])
        return D


def seidel_apsp(graph):
    """

    :param graph: sparse adjacency matrix
    :return:
    """
    n = graph.number_of_nodes()
    A = adjacency_dense(graph)
    return seidel_wiki(A, n)


def seidel_rec(A):
    """

    :param A: Adjacency matrix
    :return:
    """
    if is_complete_graph(A):
        return A
    else:
        A_sq_bool = boolean_matrix_mult(A, A)
        A_prime = np.logical_or(A_sq_bool, A).astype(int)
        np.fill_diagonal(A_prime, 0)
        D = seidel_rec(A_prime)
        DA = D @ A
        R = np.zeros(A.shape, dtype=int)
        # TODO: remove explicit loop
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                deg_j = A[j, :].sum()
                R[i][j] = 2 * D[i][j] - 1 if DA[i][j] < deg_j * D[i][j] else 2 * D[i][j]

        return R
