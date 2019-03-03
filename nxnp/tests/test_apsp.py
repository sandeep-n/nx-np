import networkx as nx

from shortest_path import *


def test_apsp():
    for num_nodes in range(10, 100, 10):
        ws_graph = nx.connected_watts_strogatz_graph(num_nodes, k=2, p=0.1)
        ws_adj_mat = nx.adj_matrix(ws_graph).toarray()
        dist_nx = np.zeros((num_nodes, num_nodes), dtype=int)
        for (s, paths) in nx.all_pairs_shortest_path(ws_graph):
            for (t, path) in paths.items():
                dist_nx[s][t] = len(path) - 1
        assert np.array_equal(seidel(ws_adj_mat), dist_nx)
