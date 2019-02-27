import itertools as it
import numpy as np


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

def triangle_count(adj):
    """
    Straightforward multiplication
    :param adj: Adjacency matrix
    :return:
    """
    return np.trace(adj @ adj @ adj) / 6


def triangle_count_3(adj):
    """
    L/U matrix splitting followed by tricks.
    :param graph:
    :return:
    """
    lu_prod = np.tril(adj) @ np.triu(adj)
    C = adj * lu_prod
    return int(np.sum(C) / 2)
