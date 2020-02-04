from random import *

def dist(A, B):
    ans = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            ans += 1
    return ans

def random_mastermind(n):
    return [randint(0, n-1) for _ in range(n)]

def perturb_one_randomly(n, tab):
    new_tab = tab.copy()
    i = randint(0,n-1)
    new_tab[i] = randint(0,n-1)
    return new_tab

