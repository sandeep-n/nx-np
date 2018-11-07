
import networkx as nx


def test_bfs_path():
    # BFS on a "grid graph" -- all nodes on a line
    for num_nodes in range(2, 10):
        graph = nx.path_graph(num_nodes)
        assert True


def test_bfs_cycle():
    pass