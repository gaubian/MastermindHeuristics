import tester
import rls
import annealing
import always_inside_mip
import one_by_one
import optimal
import greedy_best
import always_inside_backtracking
import one_plus_one_ea
import mu_lambda_ea
import mu_lambda_ga
import eda
import time
import matplotlib.pyplot as plt

def testheuristic(MAX_TIME_SECOND, MAX_PER_ITERATION, c, heuristic, args = None):
    i = 1
    ans = []
    while i <= 50:
        print(i)
        i += 1
        cur = []
        time_beginning = time.time()
        cnt = 0
        while time.time() < MAX_TIME_SECOND + time_beginning and cnt < MAX_PER_ITERATION:
            cnt += 1
            x = tester.tester(c, i, heuristic, args = args)
            cur.append(x)
        ans.append((i, cur))
        if time.time() - time_beginning > 2 * MAX_TIME_SECOND:
            break
    return ans

def plot_heuristics(c, heuristics):
    for (heur, col, MAX_TIME_SECOND, MAX_PER_ITERATION, args) in heuristics:
        x = []
        y = []
        tab = testheuristic(MAX_TIME_SECOND, MAX_PER_ITERATION, c, heur, args)
        for (i, ys) in tab:
            x = x + (len(ys) * [i])
            y = y + ys
        plt.scatter(x, y, c = col, marker = '.', label=col, alpha = 0.3)

def main_plot():
    heuristics = []
    heuristics.append((rls.heuristic, 'red', 1, 1, None))
    heuristics.append((annealing.heuristic, 'blue', 1, 1, None))
    heuristics.append((always_inside_mip.heuristic, 'orange', 30, 1, None))
    heuristics.append((one_by_one.heuristic, 'green', 1, 1, None))
    heuristics.append((optimal.heuristic, 'purple', 20, 1, None))
    heuristics.append((greedy_best.heuristic, 'cyan', 30, 1, None))
    heuristics.append((always_inside_backtracking.heuristic, 'pink', 30, 1, None))
    heuristics.append((one_plus_one_ea.heuristic, 'brown', 1, 1, None))
    #heuristics.append((mu_lambda_ea.heuristic, args=[5, 10, True]))
    #heuristics.append((mu_lambda_ea.heuristic, args=[1, 6, False]))
    #heuristics.append((mu_lambda_ga.heuristic, args=[2, 2, 0.5]))
    heuristics.append((eda.heuristic, 'gray', 1, 1, None))

    plot_heuristics(2, heuristics)
    plt.savefig("test.png")

def main():
    print(tester.tester(2, 10, rls.heuristic))
    print(tester.tester(2, 10, annealing.heuristic))
    print(tester.tester(2, 10, always_inside_mip.heuristic))
    print(tester.tester(2, 10, one_by_one.heuristic))
    print(tester.tester(3, 3, optimal.heuristic))
    print(tester.tester(3, 3, greedy_best.heuristic))
    print(tester.tester(2, 10, always_inside_backtracking.heuristic))
    print(tester.tester(2, 10, one_plus_one_ea.heuristic))
    print(tester.tester(2, 10, mu_lambda_ea.heuristic, args=[5, 10, True]))
    print(tester.tester(2, 10, mu_lambda_ea.heuristic, args=[1, 6, False]))
    print(tester.tester(2, 10, mu_lambda_ga.heuristic, args=[2, 2, 0.5]))
    print(tester.tester(2, 10, eda.heuristic))



main_plot()
