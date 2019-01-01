import networkx as nx
import numpy as np

from utils.matrixutils import adjacency_ndarray, boolean_matrix_mult


# TODO rename to something more sensible
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
    :param node: Root node, i.e., node from which to do search
    :return:
    """
    n = graph.number_of_nodes()
    A = adjacency_ndarray(graph).astype(int)

    # BFS segregates nodes into layers or levels of a search tree, according to their distance from the root.
    layers = []

    # initial layer is the root of the BFS tree
    layer = np.zeros(n, dtype=int)
    layer[node] = 1
    layers.append(set(np.nonzero(layer)[0]))

    # keep track of nodes that have been reached by the search - initially, only the root node has been visited
    visited = np.zeros(n, dtype=int)
    visited[node] = 1

    # TODO: this only works for complete graphs
    while any(x != 1 for x in visited):
        # layer contains the nodes in the next level of the BFS tree
        layer = logical_foo(boolean_matrix_mult(A, layer), visited)
        layers.append(set(np.nonzero(layer)[0]))

        visited = np.logical_or(layer, visited).astype(int)

    return layers


