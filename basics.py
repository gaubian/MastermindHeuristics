from random import *

def with_proba(p):
    return random() < p

def dist(A, B):
    ans = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            ans += 1
    return ans

def random_mastermind(c, n):
    return [randint(0, c-1) for _ in range(n)]

def random_color(c):
    return randint(0, c-1)

def crossover(n, A, B):
    C = []
    for i in range(n):
        if with_proba(0.5):
            C.append(A[i])
        else:
            C.append(B[i])
    return C

def mutate(c, n, tab):
    new_tab = tab.copy()
    for i in range(n):
        if randint(0, n-1) == 0:
            new_tab[i] = random_color(c)
    return new_tab

def perturb_one_randomly(c, n, tab):
    new_tab = tab.copy()
    i = randint(0,n-1)
    new_tab[i] = random_color(c)
    return new_tab
