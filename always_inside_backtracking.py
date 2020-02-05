from basics import *
from random import *
from math import *

def isok(remaining, capsup):
    for x in remaining:
        if x < 0 or x >= capsup:
            return False
    return True

def possible(partialsol, remaining, i, history, col, n, nbhist):
    if i == n:
        return True
    for c in range(col):
        partialsol[i] = c
        for j in range(nbhist):
            if history[j][i] == c:
                remaining[j] -= 1
        if isok(remaining, n - i) and possible(partialsol, remaining, i + 1, history, col, n, nbhist):
            return True
        for j in range(nbhist):
            if history[j][i] == c:
                remaining[j] += 1
    return False


def heuristic(c, n, score):
    history = []
    while True:
        tab = n * [0]
        inputs = list(map(lambda x : x[0], history))
        remaining = list(map(lambda x : x[1], history))
        possible(tab, remaining, 0, inputs, c, n, len(history))
        sc = score(tab)
        history.append((tab, sc))
        if sc == n:
            break
