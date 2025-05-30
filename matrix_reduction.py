import numpy as np
INF = float('inf')

def reduct(matrix: np.ndarray) -> int:
    lb = 0
    # Redukcja wierszy
    for row in matrix:
        min_val = np.min(row)
        #print(min_val)
        if min_val != INF:
            lb += min_val
            row -= min_val
    
    # Redukcja kolumn
    for col in matrix.T:
        min_val = np.min(col)
        #print(min_val)
        if min_val != INF:
            lb += min_val
            col -= min_val
    
    return lb