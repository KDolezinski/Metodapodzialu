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




# Klasa dla przechowywania podproblemu
class Podproblem:
    def __init__(self, ID, macierz, LB, sciezka, kz):
        self.ID = ID
        self.macierz = macierz
        self.LB = LB
        self.sciezka = sciezka
        self.kz = kz  # Kryterium zamknięcia (np. KZ0, KZ2, KZ3)

    def __lt__(self, other):
        return self.LB < other
    def __gt__(self,other):
        return self.LB>other
    def __eq__(self,other):
        return self.LB==other




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

def znajdz_najlepszy_zerowy(macierz):
    n = len(macierz)
    najlepszy_i = -1
    najlepszy_j = -1
    max_cena= -1

    for i in range(n):
        for j in range(n):
            if macierz[i][j] == 0:          
                min_wiersz = min([macierz[i][k] for k in range(n) if k != j and macierz[i][k] != INF])
                min_kolumna = min([macierz[k][j] for k in range(n) if k != i and macierz[k][j] != INF])
                cena = min_wiersz + min_kolumna
                if cena > max_cena:
                    max_cena = cena
                    najlepszy_i = i
                    najlepszy_j = j

    return najlepszy_i, najlepszy_j, max_cena


