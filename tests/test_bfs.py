
import networkx as nx

from bfs import bfs


def test_bfs_path():
    # BFS on a "grid graph" -- all nodes on a line -- starting from one end
    for num_nodes in range(2, 10):
        graph = nx.path_graph(num_nodes)
        true_bfs_layers = [{x} for x in range(num_nodes)]

        bfs_layers = bfs(graph, 0)
        assert bfs_layers == true_bfs_layers


def test_bfs_cycle():
    pass


def test_bfs_tree():
    pass
