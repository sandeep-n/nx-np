import networkx as nx
import numpy as np

from utils.matrixutils import adjacency_ndarray, boolean_matrix_mult


# TODO rename to more sensible
def logical_foo(v1, v2):
    """
    Not symmetric in its arguments
    :param v1:
    :param v2:
    :return:
    """
    # (0, 0) -> 0, (0, 1) -> 0, (1, 0) -> 1, (1, 1) -> 0
    visited_filter = {(0, 0): 0,
                      (0, 1): 0,
                      (1, 0): 1,
                      (1, 1): 0}
    return np.array(list(map(lambda tup: visited_filter[tup], zip(v1, v2))))


def bfs(graph, node):
    """
    Breadth First Search in matrix language
    :param graph:
    :return:
    """
    n = graph.number_of_nodes()
    A = adjacency_ndarray(graph).astype(int)

    layer = np.zeros(n, dtype=int)

    layer[node] = 1
    print(layer)

    visited = np.zeros(n, dtype=int)
    visited[node] = 1

    # TODO: this only works for complete graphs

    # while any of the nodes remains unvisited
    while any(x != 1 for x in visited):
        # layer contains the new, hitherto unvisited nodes
        layer = logical_foo(boolean_matrix_mult(A, layer), visited)
        print(layer)

        visited = np.logical_or(layer, visited).astype(int)

    return 1


