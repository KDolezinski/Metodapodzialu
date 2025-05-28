from queue import PriorityQueue
import numpy as np

INF = float('inf')

# Przykładowa macierz kosztów dla TSP (n=6)
macierz_kosztow = np.array([
    [INF, 2, 4, 6, 8, 6],
    [2, INF, 3, 2, 7, 1],
    [10, 3, INF, 1, INF, 7],
    [6, 2, 3, INF, 3, 6],
    [8, 7, INF, 3, INF, 6],
    [6, 1, 7, 10, 6, INF]
])

# Redukcja macierzy kosztów i wyznaczenie LB
def redukuj_macierz(macierz):
    lb = 0
    macierz = macierz.copy()
    
    # Redukcja wierszy
    for i in range(len(macierz)):
        min_val = np.min(macierz[i])
        if min_val != INF and not np.isinf(min_val):
            lb += min_val
            macierz[i] -= min_val
    
    # Redukcja kolumn
    for j in range(len(macierz[0])):
        min_val = np.min(macierz[:, j])
        if min_val != INF and not np.isinf(min_val):
            lb += min_val
            macierz[:, j] -= min_val
    
    return lb, macierz

# Klasa dla przechowywania podproblemu
class Podproblem:
    def __init__(self, ID, macierz, LB, sciezka, kz):
        self.ID = ID
        self.macierz = macierz
        self.LB = LB
        self.sciezka = sciezka
        self.kz = kz  # Kryterium zamknięcia 

    def __lt__(self, other):
        return self.LB < other.LB