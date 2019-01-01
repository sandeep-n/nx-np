import networkx as nx
from triangles import triangle_count_3
# import timeit
# import cProfile

# er_graph = nx.erdos_renyi_graph(500, 0.05)
# timeit.timeit(stmt='num')


def fib(n):
    """

    :param n:
    :return:
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    import timeit
    cumul_times = timeit.repeat('a = fib(42)', setup='from __main__ import fib', repeat=7, number=1000)
    print(min([x / 1000 for x in cumul_times]))
