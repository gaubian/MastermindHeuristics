from basics import *

def score(A, B, n, nb_util_ref):
    nb_util_ref[0] += 1
    ans = 0
    for i in range(n):
        if A[i] == B[i]:
            ans += 1
    return ans

def tester(n, heuristic, args = None):
    solution = random_mastermind(n)
    cnt = [0]
    if args:
        heuristic(n, lambda x : score(x, solution, n, cnt), args)
    else:
        heuristic(n, lambda x : score(x, solution, n, cnt))
    return cnt
