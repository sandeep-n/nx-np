
import networkx as nx
from scipy.special import comb

from matrixutils import adjacency_ndarray
from triangles import triangle_count


def test_triangle_count():
    for num_nodes in range(1, 10):
        graph = nx.complete_graph(num_nodes)
        adjmat = adjacency_ndarray(graph)
        # Number of triangles in a k-node complete graph is kC3 (k-choose-3)
        num_triangles = int(comb(num_nodes, 3))
        assert triangle_count(adjmat) == num_triangles
