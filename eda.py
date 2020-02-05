from random import *
from basics import *

def index_biased(tab, c, n):
    return choices(list(range(c)), weights = tab)[0]

def generate_biased(P, c, n):
    return [index_biased(P[i], c, n) for i in range(n)]

def heuristic(c, n, score):
    P = [[1/c for _ in range(c)] for _ in range(n)]
    while True:
        x = generate_biased(P, c, n)
        y = generate_biased(P, c, n)
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
            
