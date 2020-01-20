from mip import Model, xsum, BINARY

from basics import *
from random import *
from math import *

def possible(n, history):
    model = Model()
    assign = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
    for i in range(n):
        model += xsum(assign[i][j] for j in range(n)) == 1
    for (tab, sc) in history:
        model += xsum(assign[i][tab[i]] for i in range(n)) == sc
    model.optimize()
    tab = [max([(assign[i][j].x, j) for j in range(n)])[1] for i in range(n)]
    return tab

def heuristic(n, score):
    history = []
    while True:
        tab = possible(n, history)
        sc = score(tab)
        history.append((tab, sc))
        if sc == n:
            break
