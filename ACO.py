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
    nx.draw(G, with_labels=True)
    plt.show()


n = 5
matrix = create_distance_matrix(n)
create_graph(matrix, n)


class AntColony:
    def __init__(self, n, l, alpha, beta, distance):
        self.tau = [[0 for i in range(n)] for j in range(n)]
        self.probability = [[[0 for i in range(n)] for j in range(n)] for i in range(l)]  # probability[ant][i][j]
        self.cities = n
        self.ants = l
        self.alpha = alpha
        self.beta = beta
        self.distance = distance
        self.visibility = self.get_visibility()
        self.tour_length = [0 for i in range(l)]
        self.path = [[] for i in range(l)]

    def get_visibility(self):
        visibility = [[0 for i in range(n)] for j in range(n)]
        for i in range(self.cities):
            for j in range(self.cities):
                if i != j:
                    visibility[i][j] = 1/self.distance[i][j]
        return visibility

    def ant(self, ant_id):
        prev_city = np.random.randint(0, high = self.cities)
        next_city = None
        distance = 0
        for i in range(self.cities):
            next_city = move(prev_city, ant_id)
            distance += self.distance[prev_city][next_city]
        self.tour_length[ant_id] = distance



