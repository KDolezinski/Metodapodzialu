import numpy as np
from matrix_reduction import reduct
from max_out_cost import find_edge
INF = float('inf')

def subproblems(matrix: np.ndarray, lb: int=0, i: int=None, j: int=None, cost: int=None, action: str="START", path=None):
    if path is None:
        path = []
    n = matrix.shape[0]

    # Zakończenie cyklu tylko wtedy, gdy mamy pełen cykl Hamiltona!
    if len(path) == n:
        return lb, path

    if action == "START":
        lb += reduct(matrix)

        i, j, cost = find_edge(matrix)
        if cost == INF:
            return lb, path
        v1 = subproblems(matrix.copy(), lb, i, j, cost, "TAKE", path.copy())
        v2 = subproblems(matrix.copy(), lb, i, j, cost, "SKIP", path.copy())
        return v1 if v1[0] < v2[0] else v2

    if action == "TAKE":
        if cost == INF:
            return lb, path

        path.append((i, j))

        matrix[i, :] = INF
        matrix[:, j] = INF
        matrix[j, i] = INF

        lb += reduct(matrix)

        i2, j2, cost2 = find_edge(matrix)
        if cost2 == INF:
            return lb, path

        v1 = subproblems(matrix.copy(), lb, i2, j2, cost2, "TAKE", path.copy())
        v2 = subproblems(matrix.copy(), lb, i2, j2, cost2, "SKIP", path.copy())
        return v1 if v1[0] < v2[0] else v2

    if action == "SKIP":
        if cost == INF:
            return lb, path

        lb += cost
        matrix[i, j] = INF

        i2, j2, cost2 = find_edge(matrix)
        if cost2 == INF:
            return lb, path

        v1 = subproblems(matrix.copy(), lb, i2, j2, cost2, "TAKE", path.copy())
        v2 = subproblems(matrix.copy(), lb, i2, j2, cost2, "SKIP", path.copy())
        return v1 if v1[0] < v2[0] else v2

    return lb, path
