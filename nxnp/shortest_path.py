import numpy as np

from matrixutils import boolean_matrix_mult, is_complete_graph


def min_plus_apsp(adjmat):
    """
    All-pairs shortest paths using the min-plus product algorithm.
    :param graph:
    :return:
    """
    pass


def seidel(adj):
    """
    Recursive form of Seidel's algorithm for all-pairs shortest path in a connected graph with
    undirected and unweighted edges.
    :param adj: Adjacency matrix
    :return:
    """
    if is_complete_graph(adj):
        return adj
    else:
        am_sq_bool = boolean_matrix_mult(adj, adj)
        a_prime = np.logical_or(am_sq_bool, adj).astype(int)
        np.fill_diagonal(a_prime, 0)
        d = seidel(a_prime)
        da = d @ adj
        r = np.zeros(adj.shape, dtype=int)
        # TODO: remove explicit loop
        for i in range(adj.shape[0]):
            for j in range(adj.shape[1]):
                deg_j = adj[j, :].sum()
                r[i][j] = 2 * d[i][j] - 1 if da[i][j] < deg_j * d[i][j] else 2 * d[i][j]

        return r
