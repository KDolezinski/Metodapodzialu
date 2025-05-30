import numpy as np
from subproblems import subproblems
from matrix_reduction import reduct
from max_out_cost import find_edge
INF = float('inf')

A = np.array([
    [INF, 2, 4, 6, 8, 6],
    [2, INF, 3, 2, 7, 1],
    [10, 3, INF, 1, INF, 7],
    [6, 2, 3, INF, 3, 6],
    [8, 7, INF, 3, INF, 6],
    [6, 1, 7, 10, 6, INF]
])
A = np.array([
    [INF,5,4,6,6],
    [8,INF,5,3,4],
    [4,3,INF,3,1],
    [8,2,5,INF,6],
    [2,2,7,0,INF]
])
# A = np.array([
#     [INF, 10, 8, 19, 12],
#     [10, INF, 20, 6, 3],
#     [8, 20, INF, 4, 2],
#     [19, 6, 4, INF, 7],
#     [12, 3, 2, 7, INF]
# ])
matrix = A.copy()

out_val, path = subproblems(matrix)
print("Macierz kosztów:")
print(A)
print("Minimalny koszt:", out_val)
print(path)
d = dict(path)
k0 = path[0][0]
v = d[k0]
final_path = [str(k0+1),str(v+1)]
while v != k0:
    v = d[v]
    final_path.append(str(v+1))
print("Ścieżka:",  " -> ".join(final_path) )