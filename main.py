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

def main():
    print(tester.tester(2, 10, rls.heuristic))
    print(tester.tester(2, 10, annealing.heuristic))
    #print(tester.tester(10, 10, always_inside_mip.heuristic))
    print(tester.tester(2, 10, one_by_one.heuristic))
    print(tester.tester(3, 3, optimal.heuristic))
    print(tester.tester(3, 3, greedy_best.heuristic))
    #print(tester.tester(10, 10, always_inside_backtracking.heuristic))
    print(tester.tester(2, 10, one_plus_one_ea.heuristic))
    print(tester.tester(2, 10, mu_lambda_ea.heuristic, args=[5, 10, True]))
    print(tester.tester(2, 10, mu_lambda_ea.heuristic, args=[1, 6, False]))
    print(tester.tester(2, 10, mu_lambda_ga.heuristic, args=[2, 2, 0.5]))
    print(tester.tester(2, 10, eda.heuristic))



main()
