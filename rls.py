from basics import *

def heuristic(n, score):
    tab = random_mastermind(n)
    sc = score(tab)
    while sc != n:
        new_tab = perturb_one_randomly(n, tab)
        new_sc = score(new_tab)
        if new_sc >= sc:
            tab = new_tab
            sc = new_sc
