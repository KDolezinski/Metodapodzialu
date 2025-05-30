import numpy as np
from subproblems import subproblems
INF = float('inf')

# macierz_kosztow = np.array([
#     [INF, 2, 4, 6, 8, 6],
#     [2, INF, 3, 2, 7, 1],
#     [10, 3, INF, 1, INF, 7],
#     [6, 2, 3, INF, 3, 6],
#     [8, 7, INF, 3, INF, 6],
#     [6, 1, 7, 10, 6, INF]
# ])
A = np.array([
    [INF,5,4,6,6],
    [8,INF,5,3,4],
    [4,3,INF,3,1],
    [8,2,5,INF,6],
    [2,2,7,0,INF]
])

out_val, path = subproblems(A.copy())
print("Macierz kosztów:")
print(A)
print("Minimalny koszt:", out_val)
print("Ścieżka (krawędzie):", path)
