# Helper functions for adjacency matrices
import networkx as nx
import numpy as np


def adjacency_ndarray(graph):
    """
    The adjacency matrix of a networkx graph in numpy's ndarray format.
    :param graph: an undirected graph
    :type graph: nx.Graph
    :return: Graph's adjacency matrix in np.ndarray format
    """
    # TODO: doesn't work when nodes are not labeled by 0-indexed integers.
    num_nodes = graph.number_of_nodes()
    adj_mat = np.zeros((num_nodes, num_nodes))
    for (u, v) in graph.edges:
        adj_mat[u][v] = 1
        adj_mat[v][u] = 1

    return adj_mat


def adjacency_dense(graph):
    """
    The networkx function nx.adjacency_matrix gives the adjacency matrix in sparse
    matrix format. Use this function if desired in dense format.
    :param graph:
    :type graph: nx.Graph
    :return: ndarray
    """
    sparse_adj_matrix = nx.adjacency_matrix(graph)
    return sparse_adj_matrix.toarray()


def boolean_matrix_mult(a, b):
    """

    :param a: 0-1 matrix
    :param b: 0-1 matrix
    :return:
    """
    A_bool = a.astype('bool')
    B_bool = b.astype('bool')
    C_bool = A_bool @ B_bool
    C = C_bool.astype('int32')
    return C


def complete_graph_matrix(n):
    """
    Returns a matrix corresponding to a complete graph of n nodes. Such a matrix has 0 on the diagonal and 1 elsewhere.
    :param n: Number of nodes
    :return: np.ndarray
    """
    adj_mat = np.ones(shape=(n, n), dtype=int)
    np.fill_diagonal(adj_mat, 0)  # in-place operation!
    return adj_mat


def is_complete_graph(a):
    """
    Test if a given matrix is an adjacency matrix of a complete graph.
    :param a:
    :return:
    """
    # Test that diagonals are 0
    cond_1 = np.all(a.diagonal() == 0)
    # Test that off-diagonals are 1
    off_diagonal_index = np.where(~np.eye(a.shape[0], dtype=bool))
    cond_2 = a[off_diagonal_index].all()
    return cond_1 and cond_2


def degree(a, j):
    """

    :param a: adjacency matrix
    :param j: node in graph
    :return: degree of node j
    """

    return a[j, :].sum()


def matrix_power(a, k):
    """
    Raise matrix A to the power k by repeated squaring
    :param a: Square matrix A
    :param k:
    :return:
    """
    if k == 0:
        return np.identity(a.shape[0], dtype='int32')
    elif k == 1:
        return a
    else:
        if k % 2 == 0:
            return matrix_power(a @ a, k // 2)
        else:
            return matrix_power(a @ a, k // 2) @ a
