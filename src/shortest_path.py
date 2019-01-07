
import numpy as np

from utils.matrixutils import adjacency_dense, boolean_matrix_mult, is_complete_graph


def min_plus_apsp(graph):
    """
    All-pairs shortest paths using the min-plus product algorithm.
    :param graph:
    :return:
    """
    pass


def seidel(am):
    """
    Recursive form of Seidel's algorithm for all-pairs shortest path in a connected graph with
    undirected and unweighted edges.
    :param am: Adjacency matrix
    :return:
    """
    if is_complete_graph(am):
        return am
    else:
        am_sq_bool = boolean_matrix_mult(am, am)
        a_prime = np.logical_or(am_sq_bool, am).astype(int)
        np.fill_diagonal(a_prime, 0)
        d = seidel(a_prime)
        da = d @ am
        r = np.zeros(am.shape, dtype=int)
        # TODO: remove explicit loop
        for i in range(am.shape[0]):
            for j in range(am.shape[1]):
                deg_j = am[j, :].sum()
                r[i][j] = 2 * d[i][j] - 1 if da[i][j] < deg_j * d[i][j] else 2 * d[i][j]

        return r
