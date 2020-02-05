from mip import Model, xsum, BINARY, minimize

from basics import *
from random import *
from math import *

def possible(c, n, history):
    model = Model()
    model.verbose = 0
    assign = [[model.add_var(var_type=BINARY) for j in range(c)] for i in range(n)]
    for i in range(n):
        model += xsum(assign[i][j] for j in range(c)) == 1
    for (tab, sc) in history:
        model += xsum(assign[i][tab[i]] for i in range(n)) == sc
    model.optimize()
    tab = [max([(assign[i][j].x, j) for j in range(c)])[1] for i in range(n)]
    return tab

def heuristic(c, n, score):
    history = []
    while True:
        tab = possible(c, n, history)
        sc = score(tab)
        history.append((tab, sc))
        if sc == n:
            break
