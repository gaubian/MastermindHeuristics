from basics import *

def heuristic(n, score):
    tab = random_mastermind(n)
    sc = score(tab)
    while sc != n:
        new_tab = tab.copy()
        for i in range(n):
            if randint(0, n-1) == 0:
                new_tab[i] = random_color(n)
        new_sc = score(new_tab)
        if new_sc >= sc:
            tab = new_tab
            sc = new_sc
