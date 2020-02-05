from random import *
from basics import *

def index_biased(tab, n):
    return choices(list(range(n)), weights = tab)[0]

def generate_biased(P, n):
    return [index_biased(P[i], n) for i in range(n)]

def heuristic(c, n, score):
    P = [[1/c for _ in range(c)] for _ in range(n)]
    while True:
        x = generate_biased(P, n)
        y = generate_biased(P, n)
        sc_x = score(x)
        sc_y = score(y)
        if sc_x < sc_y:
            x, y = y, x
            sc_x, sc_y = sc_y, sc_x
        if sc_x == n:
            break
        for i in range(n):
            P[i][y[i]] /= 2
            P[i][x[i]] += P[i][y[i]]
            
