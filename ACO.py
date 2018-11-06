import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def create_distance_matrix(n):
    a = np.random.randint(1, high=100, size=(n, n))
    print(a)
    return a


def create_graph(matrix, n):
    G = nx.Graph()
    for i in range(n):
        for j in range(n):
            G.add_edge(i, j)
            G[i][j]['weight'] = matrix[i][j]
    nx.draw(G)
    plt.show()


n = 5
matrix = create_distance_matrix(n)
create_graph(matrix, n)
