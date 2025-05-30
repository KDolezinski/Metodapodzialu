import numpy as np


def find_edge(matrix:np.ndarray) -> tuple[int, int, int]:
    best_i = -1
    best_j = -1
    max_cost = -1
    rows, cols = matrix.shape
    for i in  range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                cost = np.min([matrix[i, k] for k in range(cols) if k != j]) + np.min([matrix[k, j] for k in range(rows) if k != i])
                if cost > max_cost:
                    max_cost = cost
                    best_i = i
                    best_j = j

    return best_i, best_j, max_cost