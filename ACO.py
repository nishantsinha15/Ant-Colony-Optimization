import math

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
            if i == j:
                continue
            G.add_edge(i, j)
            G[i][j]['weight'] = matrix[i][j]
    nx.draw(G, with_labels=True)
    # plt.savefig('visualize'+str(n)+'.png')
    plt.clf()

class AntColony:
    def __init__(self, distance, n=4, l=10, alpha=1, beta=3, rho=0.8, Q=1, iterations=100):
        self.tau = [[0 for i in range(n)] for j in range(n)]
        self.cities = n
        self.ants = l
        self.alpha = alpha
        self.beta = beta
        self.distance = distance
        self.visibility = self.get_visibility()
        self.tour_length = [0 for i in range(l)]
        self.path = [[] for i in range(l)]
        self.visited = [[] for i in range(l)]
        self.rho = rho
        self.Q = Q
        self.iterations = iterations

    def get_visibility(self):
        visibility = [[0 for i in range(n)] for j in range(n)]
        for i in range(self.cities):
            for j in range(self.cities):
                if i != j:
                    visibility[i][j] = 1 / self.distance[i][j]
        return visibility

    def ant(self, ant_id, iter):
        prev_city = np.random.randint(0, high=self.cities)
        next_city = np.random.randint(0, high=self.cities)
        distance = 0
        self.visited[ant_id].append(prev_city)
        for i in range(self.cities-1):
            if iter == 0:
                while next_city == prev_city:
                    next_city = np.random.randint(0, high=self.cities)
            else:
                next_city = self.move(prev_city, ant_id)
            distance += self.distance[prev_city][next_city]
            self.path[ant_id].append((prev_city, next_city))
            self.visited[ant_id].append(next_city)
            prev_city = next_city
        self.tour_length[ant_id] = distance

    def move(self, prev_city, ant_id):
        probability = [0 for i in range(self.cities)]
        for j in range(self.cities):
            if j not in self.visited[ant_id]:
                probability[j] = math.pow(self.tau[prev_city][j], self.alpha) * math.pow(
                    self.visibility[prev_city][j], self.beta)
            else:
                probability[j] = 0
        next_city = np.random.choice(a=[i for i in range(self.cities)], p=np.divide(probability, sum(probability)))
        return next_city

    def update_tau(self):
        for i in range(self.cities):
            for j in range(self.cities):
                if i == j:
                    continue
                delta = 0
                for ant_id in range(self.ants):
                    if (i, j) in self.path[ant_id] or (j, i) in self.path[ant_id]:
                        delta += self.Q / self.tour_length[ant_id]
                self.tau[i][j] = self.rho * self.tau[i][j] + delta

    def reset(self):
        self.tour_length = [0 for i in range(self.ants)]
        self.path = [[] for i in range(self.ants)]
        self.visited = [[] for i in range(self.ants)]

    def solve(self):
        temp = []
        for i in range(self.iterations):
            self.reset()
            for ant_id in range(self.ants):
                self.ant(ant_id, i)
            self.update_tau()
            print(sum(self.tour_length) / len(self.tour_length))
            temp.append(sum(self.tour_length) / len(self.tour_length))
        print("Printing path")
        for i in self.path:
            print(i)
        self.plot(temp)

    def plot(self, a):
        plt.plot(a)
        plt.show()

# for i in range(3, 10):
#     matrix = create_distance_matrix(i)
#     create_graph(matrix, i)
i = 5
n = 5
matrix = create_distance_matrix(i)
create_graph(matrix, i)
a = AntColony(matrix)
a.solve()