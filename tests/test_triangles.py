import networkx as nx
from scipy.special import comb

from triangles import triangle_count_3


def test_triangle_count_3():
    for num_nodes in range(1, 10):
        complete_graph = nx.complete_graph(num_nodes)
        # Number of triangles in a k-node complete graph is kC3 (k-choose-3)
        num_triangles = int(comb(num_nodes, 3))
        assert triangle_count_3(complete_graph) == num_triangles


def test_apsp():
    for num_nodes in range(10, 100, 10):
        er_graph = nx.erdos_renyi_graph(num_nodes, 0.10)
    pass


def test_bfs():
    pass
