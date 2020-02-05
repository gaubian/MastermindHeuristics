from basics import *

def heuristic(n, score, args):
    mu = args[0]
    lamb = args[1]
    c = args[2]
    x = []
    for _ in range(mu):
        mem = random_mastermind(n)
        x.append((score(mem), mem))
    while True:
        y = []
        for _ in range(lamb):
            new_tab = []
            if with_proba(c):
                i = randint(0, mu - 1)
                new_tab = mutate(n, x[i][1])
            else:
                i = randint(0, mu - 1)
                j = randint(0, mu - 1)
                new_tab = crossover(n, x[i][1], x[j][1])
            y.append((score(new_tab), new_tab))
        x = x + y
        x = list((reversed(sorted(x))))[:mu]
        if x[0][0] == n:
            break
