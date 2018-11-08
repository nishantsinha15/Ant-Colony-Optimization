import pants
import math
import random

n = 10

nodes = []
for _ in range(n):
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    nodes.append((x, y))


def euclidean(a, b):
    return math.sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))


world = pants.World(nodes, euclidean)
solver = pants.Solver()
solution = solver.solve(world)
# or
solutions = solver.solutions(world)
print(solution.distance)
print(solution.tour)
print(solution.path)    # Edges taken in order
# or
for s in solutions:
  print(s.distance)