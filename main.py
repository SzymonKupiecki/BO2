import random

import numpy as np
from dtypes import matrix_to_solve
from Szymon import sample_matrix_generator, is_valid, optimize
from solution import Solution

# sample data
hard_matrix = [[0, 20, 10, 15, 80, 60],
               [20,  0, 10, 40, 15, 10],
               [10, 10,  0,  5, 30, 20],
               [15, 40,  5,  0, 40, 25],
               [80, 15, 30, 40,  0, 5],
               [60, 10, 20,  25,  5, 0]]


cable_vector = [(0.15, 10), (0.25, 20), (0.5, 40)]

cost_tuples = [(0, 0, 0), (90, 300, 15), (110, 450, 70), (80, 150, 40), (70, 250, 20), (120, 100, 90)]

info = matrix_to_solve(np.array(hard_matrix)*0.01, np.array(cable_vector), np.array(cost_tuples))

starting_solution = Solution(sample_matrix_generator(0, 6, 3, 0.8), info)
random.seed(None)
res = optimize(starting_solution, info)
print(res)
