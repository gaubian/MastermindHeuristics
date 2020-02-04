from basics import *

def heuristic(n, score):
    tab = random_mastermind(n)
    sc = score(tab)
    for i in range(n):
        while True:
            tab[i] = (tab[i] + 1) % n
            new_sc = score(tab)
            if new_sc < sc:
                tab[i] = (tab[i] + n - 1) % n
                break
            if new_sc > sc:
                sc = new_sc
                break
