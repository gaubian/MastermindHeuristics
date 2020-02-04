import itertools

from basics import *
from random import *
from math import *

def f(n, inp, all_poss):
    best_move = (n - 1, inp[0])
    for x in all_poss:
        ma = dict()
        for y in inp:
            d = dist(x, y)
            if d not in ma:
                ma[d] = 0
            ma[d] += 1
        maxi = 0
        for (_, b) in ma.items(): 
            maxi = max(maxi, b)
        best_move = min(best_move, (maxi , x))
    return best_move[1]

def generate_all_poss(n):
    l = [list(range(n)) for i in range(n)]
    return list(map(tuple, list(itertools.product(*l))))

def extract(x, sc, list_poss):
    ans = []
    for y in list_poss:
        if(dist(x, y) == sc):
            ans.append(y)
    return ans

def heuristic(n, score):
    all_poss = generate_all_poss(n)
    inp = all_poss
    while True:
        if len(inp) == 1:
            break
        x = f(n, inp, all_poss)
        sc = score(x)
        inp = extract(x, sc, inp)

