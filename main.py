import tester
import rls
import annealing
import always_inside_mip
import one_by_one
import optimal
import greedy_best
import always_inside_backtracking
import one_plus_one_ea

def main():
    print(tester.tester(10, rls.heuristic))
    print(tester.tester(10, annealing.heuristic))
    print(tester.tester(10, always_inside_mip.heuristic))
    print(tester.tester(10, one_by_one.heuristic))
    print(tester.tester(3, optimal.heuristic))
    print(tester.tester(3, greedy_best.heuristic))
    print(tester.tester(10, always_inside_backtracking.heuristic))
    print(tester.tester(10, one_plus_one_ea.heuristic))

main()
