import itertools

from basics import *
from random import *
from math import *

def f(n, dyn, inp, all_poss):
    if len(inp) == 1:
            return (0, inp[0])
    if inp in dyn:
        return dyn[inp]
    dyn[inp] = (len(all_poss) - 1, inp[0])
    best_move = (n - 1, inp[0])
    for x in all_poss:
        ma = dict()
        for y in inp:
            d = dist(x, y)
            if d not in ma:
                ma[d] = []
            ma[dist(x, y)].append(y)
        maxi = 0
        for (a, b) in ma.items(): 
            maxi = max(maxi, (f(n, dyn, tuple(b), all_poss))[0])
        best_move = min(best_move, (maxi , x))
    dyn[inp] = best_move
    return best_move

def generate_all_poss(n):
    l = [list(range(n)) for i in range(n)]
    return list(map(tuple, list(itertools.product(*l))))

def extract(x, sc, list_poss):
    ans = []
    for y in list_poss:
        if(dist(x, y) == sc):
            ans.append(y)
    return tuple(ans)

def heuristic(n, score):
    all_poss = generate_all_poss(n)
    inp = tuple(all_poss)
    dyn = dict()
    while True:
        if len(inp) == 1:
            break
        (_, x) = f(n, dyn, inp, all_poss)
        sc = score(x)
        inp = extract(x, sc, inp)

