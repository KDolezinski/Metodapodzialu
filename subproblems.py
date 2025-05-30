import numpy as np
from matrix_reduction import reduct
from max_out_cost import find_edge
from typing import List, Tuple
INF = float('inf')

def subproblems(matrix: np.ndarray, lb: int = 0, i: int = None, j: int = None, cost: int = None,
                 action: str = "START", path=None, compare_lb=INF):
    if path is None:
        path = []

    if action == "START":
        r = reduct(matrix)
        lb += r
        print("LB =",r)
        i, j, cost = find_edge(matrix)
        if i == -1 or j == -1:
            return INF, path
        res1 = subproblems(matrix.copy(), lb, i, j, cost, "TAKE", path.copy())
        res2 = subproblems(matrix.copy(), lb, i, j, cost, "SKIP", path.copy(), res1[0])
        return min(res1, res2, key=lambda x: x[0])
        #return res1

    if action == "TAKE":
        path_copy = path.copy()
        path_copy.append((i, j))
        check_cycle(path_copy, matrix)
        matrix_copy = matrix.copy()
        matrix_copy[i, :] = INF
        matrix_copy[:, j] = INF
        matrix_copy[j, i] = INF

        lb += reduct(matrix_copy)

        ni, nj, ncost = find_edge(matrix_copy)
        if ni == -1 or nj == -1:
            if np.all(matrix_copy == INF):
                return lb, path_copy
            else:
                return INF, path_copy

        res1 = subproblems(matrix_copy, lb, ni, nj, ncost, "TAKE", path_copy)
        res2 = subproblems(matrix_copy, lb, ni, nj, ncost, "SKIP", path_copy, res1[0])
        return min(res1, res2, key=lambda x: x[0])
    
    if action == "SKIP":
        matrix_copy = matrix.copy()
        matrix_copy[i, j] = INF

        lb += cost
        if lb >= compare_lb:
            return INF, path

        lb += reduct(matrix_copy)

        ni, nj, ncost = find_edge(matrix_copy)
        if ni == -1 or nj == -1:
            if np.all(matrix_copy == INF):
                return lb, path
            else:
                return INF, path

        res1 = subproblems(matrix_copy, lb, ni, nj, ncost, "TAKE", path.copy())
        res2 = subproblems(matrix_copy, lb, ni, nj, ncost, "SKIP", path.copy(), res1[0])
        return min(res1, res2, key=lambda x: x[0])

    return INF, path

def check_cycle(path:List[Tuple[int,int]],matrix:np.ndarray) -> bool:
    if len(path) == 1 or len(path) == 0 or len(path) == len(matrix):
        return 
    print(path)
    d = dict(path)
    longest_path = []
    for k0 in d.keys():
        v = d.get(k0, None)
        cycle_alert = [k0]
        while True and v is not None:
            cycle_alert.append(v)
            
            v = d.get(v, None)
        if v is not None:
            cycle_alert.append(v)
        if len(cycle_alert) < 3:
            continue
        if len(cycle_alert) > len(longest_path):
            longest_path = cycle_alert
    print("CYCLE DETECTED:", longest_path)
    if len(longest_path) == len(matrix):
        to_remove = longest_path[1:-2]
    else:
        to_remove = longest_path[:-2]
    for el in to_remove:
         matrix[longest_path[-1],el] = INF
         print("INF for:", longest_path[-1], el)
    print("")

