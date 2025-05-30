import numpy as np


def find_edge(matrix:np.ndarray) -> tuple[int, int, int]:
    best_i = -1
    best_j = -1
    max_cost = -1
    rows, cols = matrix.shape
    for i in  range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                cost = np.min(matrix[i, :],where=matrix[i, :] > 0,initial=np.inf) + np.min(matrix[:, j],where=matrix[:, j] > 0,initial=np.inf)
                if cost >= max_cost:
                    if cost == np.inf:
                        return -1, -1, np.inf
                    max_cost = cost
                    best_i = i
                    best_j = j

    return best_i, best_j, max_cost