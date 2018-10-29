import itertools as it
import networkx as nx
import numpy as np

from utils.matrixutils import adjacency_ndarray


def triangle_count_iter(graph):
    """
    Without over-counting
    :param graph: networkx graph
    :return: number of triangles
    """
    num_triangles = 0

    for v in graph.nbunch_iter():
        neighbor_pairs = it.combinations(graph.neighbors(v), 2)
        for (u, w) in neighbor_pairs:
            if v < u < w:
                if (u, w) in graph.edges:
                    num_triangles += 1

    return num_triangles


# def node_iterator_plusplus(graph):
#     """
#
#     :param graph:
#     :return:
#     """
#     num_triangles = 0
#     degree_sorted_nodes = sorted(graph.nodes, key=graph.degree())
#     rank = dict((y, x) for (x, y) in enumerate(degree_sorted_nodes))
#     for v in graph.nodes:
#         for u in [ngbr for ngbr in graph.neighbors(v) if rank[ngbr] > rank[v]]:
#             for w in [ngbr for ngbr in graph.neighbors(v) if rank[ngbr] > rank[u]]:
#                 if (u, w) in graph.edges:
#                     num_triangles += 1
#     return num_triangles

# the linear algebra way

def triangle_count_2(graph):
    """
    Straightforward multiplication
    :param graph:
    :return:
    """
    A = adjacency_ndarray(graph)
    return np.trace(A @ A @ A) / 6


def triangle_count_3(graph):
    """
    L/U matrix splitting followed by tricks.
    :param graph:
    :return:
    """
    A = adjacency_ndarray(graph)
    B = np.tril(A) @ np.triu(A)
    C = A * B
    return int(np.sum(C) / 2)
