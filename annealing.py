from basics import *
from random import *
from math import *

def heuristic(n, score):
    tab = random_mastermind(n)
    sc = score(tab)
    i = 0
    while sc != n:
        new_tab = perturb_one_randomly(n, tab)
        new_sc = score(new_tab)
        if new_sc >= sc or random() < exp((new_sc - sc)*i):
            tab = new_tab
            sc = new_sc
        i += 1
