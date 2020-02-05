from basics import *

def heuristic(c, n, score):
    tab = random_mastermind(c, n)
    sc = score(tab)
    for i in range(n):
        while True:
            tab[i] = (tab[i] + 1) % c
            new_sc = score(tab)
            if new_sc < sc:
                tab[i] = (tab[i] + c - 1) % c
                break
            if new_sc > sc:
                sc = new_sc
                break
