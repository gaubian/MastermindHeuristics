import matplotlib
matplotlib.use('Agg')

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

def testheuristic(MAX_I, MAX_TIME_SECOND, MAX_PER_ITERATION, c_func, heuristic, args = None):
    i = 1
    ans = []
    while i <= MAX_I:
        print(i)
        i += 1
        cur = []
        time_beginning = time.time()
        cnt = 0
        while time.time() < MAX_TIME_SECOND + time_beginning and cnt < MAX_PER_ITERATION:
            cnt += 1
            x = tester.tester(c_func(i), i, heuristic, args = args)
            cur.append(x)
        ans.append((i, cur))
        if time.time() - time_beginning > 2 * MAX_TIME_SECOND:
            break
    return ans

def plot_heuristics(c_func, heuristics, MAX_I = 50, alpha = 0.3):
    fig, ax = plt.subplots()
    for (heur, col, MAX_TIME_SECOND, MAX_PER_ITERATION, args, name, plot_avg) in heuristics:
        x = []
        y = []
        tab = testheuristic(MAX_I, MAX_TIME_SECOND, MAX_PER_ITERATION, c_func, heur, args)
        for (i, ys) in tab:
            if plot_avg:
                x.append(i)
                y.append(sum(ys) / len(ys))
            else:
                x = x + (len(ys) * [i])
                y = y + ys
        ax.scatter(x, y, c = col, marker = '.', label=name, alpha = alpha)
    ax.legend()

def greedy_plot():
    heuristics = []
    heuristics.append((greedy_best.heuristic, 'red', 1, 100, None, 'Greedy', True))
    plot_heuristics(lambda sz : 2, heuristics, alpha = 1)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("greedy_plot.png")

def rls_plot_one_max():
    heuristics = []
    heuristics.append((rls.heuristic, 'red', 1, 100, none, 'rls iterations', false))
    heuristics.append((rls.heuristic, 'blue', 1, 100, none, 'rls average', true))
    plot_heuristics(lambda sz : 2, heuristics, max_i = 100)
    plt.xlabel('n')
    plt.ylabel('number of queries')
    plt.savefig("rls_plot.png")

def rls_plot_mastermind_n_color():
    heuristics = []
    heuristics.append((rls.heuristic, 'red', 20, 20, None, 'RLS iterations', False))
    heuristics.append((rls.heuristic, 'blue', 20, 20, None, 'RLS average', True))
    plot_heuristics(lambda sz : sz, heuristics, MAX_I = 100)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("rls_plot_n_color.png")

def eda_plot():
    heuristics = []
    heuristics.append((eda.heuristic, 'red', 10, 10, None, 'EDA iterations', False))
    heuristics.append((eda.heuristic, 'blue', 10, 10, None, 'EDA average', True))
    plot_heuristics(lambda sz : sz, heuristics, MAX_I = 25)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("eda_plot_n_color.png")

def annealing_plot_one_max():
    heuristics = []
    heuristics.append((annealing.heuristic, 'red', 10, 20, None, 'Annealing iterations', False))
    heuristics.append((annealing.heuristic, 'blue', 10, 20, None, 'Annealing average', True))
    plot_heuristics(lambda sz : 2, heuristics, MAX_I = 100)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("annealing_one_max.png")

def annealing_plot_n_color():
    heuristics = []
    heuristics.append((annealing.heuristic, 'red', 10, 20, None, 'Annealing iterations', False))
    heuristics.append((annealing.heuristic, 'blue', 10, 20, None, 'Annealing average', True))
    plot_heuristics(lambda sz : sz, heuristics)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("annealing_n_color.png")

def one_by_one_plot_one_max():
    heuristics = []
    heuristics.append((one_by_one.heuristic, 'red', 10, 100, None, 'One by one iterations', False))
    heuristics.append((one_by_one.heuristic, 'blue', 10, 100, None, 'One by one average', True))
    plot_heuristics(lambda sz : 2, heuristics, MAX_I = 100)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("one_by_one_one_max.png")

def one_by_one_plot_n_color():
    heuristics = []
    heuristics.append((one_by_one.heuristic, 'red', 10, 20, None, 'One by one iterations', False))
    heuristics.append((one_by_one.heuristic, 'blue', 10, 20, None, 'One by one average', True))
    plot_heuristics(lambda sz : sz, heuristics, MAX_I = 100)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("one_by_one_n_color.png")

def backtracking_plot_one_max():
    heuristics = []
    heuristics.append((always_inside_backtracking.heuristic, 'blue', 10, 10, None, 'Backtracking', True))
    plot_heuristics(lambda sz : 2, heuristics, MAX_I = 30)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("backtracking_one_max.png")

def mip_plot_one_max():
    heuristics = []
    heuristics.append((always_inside_mip.heuristic, 'blue', 10, 1, None, 'MIP', True))
    plot_heuristics(lambda sz : 2, heuristics, MAX_I = 25)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("mip_one_max.png")

def mip_plot_n_color():
    heuristics = []
    heuristics.append((always_inside_mip.heuristic, 'blue', 10, 1, None, 'MIP', True))
    plot_heuristics(lambda sz : sz, heuristics, MAX_I = 25)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("mip_n_color.png")

def mu_lambda_one_max():
    heuristics = []
    heuristics.append((mu_lambda_ea.heuristic, 'red', 10, 10, [1, 6, False], '(mu, lambda) EA iterations', False))
    heuristics.append((mu_lambda_ea.heuristic, 'blue', 10, 10, [1, 6, False], '(mu, lambda) EA average', True))
    plot_heuristics(lambda sz : 2, heuristics)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("mu_lambda_one_max.png")

def mu_lambda_n_color():
    heuristics = []
    heuristics.append((mu_lambda_ea.heuristic, 'red', 10, 10, [1, 6, False], '(mu, lambda) EA iterations', False))
    heuristics.append((mu_lambda_ea.heuristic, 'blue', 10, 10, [1, 6, False], '(mu, lambda) EA average', True))
    plot_heuristics(lambda sz : sz, heuristics, MAX_I = 20)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("mu_lambda_n_color.png")

def mu_plus_lambda_one_max():
    heuristics = []
    heuristics.append((mu_lambda_ea.heuristic, 'red', 10, 10, [5, 10, True], '(mu + lambda) EA iterations', False))
    heuristics.append((mu_lambda_ea.heuristic, 'blue', 10, 10, [5, 10, True], '(mu + lambda) EA average', True))
    plot_heuristics(lambda sz : 2, heuristics)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("mu_plus_lambda_one_max.png")

def mu_plus_lambda_n_color():
    heuristics = []
    heuristics.append((mu_lambda_ea.heuristic, 'red', 10, 10, [5, 10, True], '(mu + lambda) EA iterations', False))
    heuristics.append((mu_lambda_ea.heuristic, 'blue', 10, 10, [5, 10, True], '(mu + lambda) EA average', True))
    plot_heuristics(lambda sz : sz, heuristics, MAX_I = 25)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("mu_plus_lambda_n_color.png")

def mu_lambda_ga_one_max():
    heuristics = []
    heuristics.append((mu_lambda_ea.heuristic, 'red', 10, 10, [2, 2, 0.5], '(mu + lambda) GA iterations', False))
    heuristics.append((mu_lambda_ea.heuristic, 'blue', 10, 10, [2, 2, 0.5], '(mu + lambda) GA average', True))
    plot_heuristics(lambda sz : 2, heuristics)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("mu_plus_lambda_ga_one_max.png")

def mu_lambda_ga_n_color():
    heuristics = []
    heuristics.append((mu_lambda_ea.heuristic, 'red', 10, 10, [2, 2, 0.5], '(mu + lambda) GA iterations', False))
    heuristics.append((mu_lambda_ea.heuristic, 'blue', 10, 10, [2, 2, 0.5], '(mu + lambda) GA average', True))
    plot_heuristics(lambda sz : sz, heuristics, MAX_I = 25)
    plt.xlabel('n')
    plt.ylabel('Number of queries')
    plt.savefig("mu_plus_lambda_ga_n_color.png")

def main_plot():
    heuristics = []
    heuristics.append((rls.heuristic, 'red', 1, 1, None, 'RLS', True))
    heuristics.append((annealing.heuristic, 'blue', 1, 1, None, 'annealing', True))
    heuristics.append((always_inside_mip.heuristic, 'orange', 30, 1, None, 'MIP', True))
    heuristics.append((one_by_one.heuristic, 'green', 1, 1, None, 'One by one', True))
    #heuristics.append((optimal.heuristic, 'purple', 10, 1, None, 'Optimal', True))
    #heuristics.append((greedy_best.heuristic, 'cyan', 10, 1, None, 'Greedy best', True))
    heuristics.append((always_inside_backtracking.heuristic, 'pink', 30, 1, None, 'Backtracking', True))
    heuristics.append((one_plus_one_ea.heuristic, 'brown', 1, 1, None, '1+1 ea', True))
    heuristics.append((mu_lambda_ea.heuristic, 'black', 1, 1, [5, 10, True], 'mu+lambda ea', True))
    heuristics.append((mu_lambda_ea.heuristic, 'yellow', 1, 1, [1, 6, False], 'mu,lambda ea', True))
    heuristics.append((mu_lambda_ga.heuristic, 'orange', 1, 1, [2, 2, 0.5], 'mu+lambda ga', True))
    heuristics.append((eda.heuristic, 'gray', 1, 1, None, 'EDA', True))

    plot_heuristics(lambda sz : 2, heuristics)
    plt.savefig("final_plot_one_max.png")

def main():
    print(tester.tester(2, 10, rls.heuristic))
    print(tester.tester(2, 10, annealing.heuristic))
    print(tester.tester(2, 10, always_inside_mip.heuristic))
    print(tester.tester(2, 10, one_by_one.heuristic))
    #print(tester.tester(3, 3, optimal.heuristic))
    #print(tester.tester(3, 3, greedy_best.heuristic))
    print(tester.tester(2, 10, always_inside_backtracking.heuristic))
    print(tester.tester(2, 10, one_plus_one_ea.heuristic))
    print(tester.tester(2, 10, mu_lambda_ea.heuristic, args=[5, 10, True]))
    print(tester.tester(2, 10, mu_lambda_ea.heuristic, args=[1, 6, False]))
    print(tester.tester(2, 10, mu_lambda_ga.heuristic, args=[2, 2, 0.5]))
    print(tester.tester(2, 10, eda.heuristic))

main_plot()
