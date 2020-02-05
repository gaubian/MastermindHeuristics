from basics import *

def heuristic(c, n, score, args):
    mu = args[0]
    lamb = args[1]
    plus = args[2]
    x = []
    for _ in range(mu):
        mem = random_mastermind(c, n)
        x.append((score(mem), mem))
    while True:
        y = []
        for _ in range(lamb):
            i = randint(0, mu - 1)
            new_tab = mutate(c, n, x[i][1])
            y.append((score(new_tab), new_tab))
        if plus:
            x = x + y
        else:
            x = y
        x = list((reversed(sorted(x))))[:mu]
        if x[0][0] == n:
            break
