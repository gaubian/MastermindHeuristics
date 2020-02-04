import tester
import rls
import annealing
import always_inside_mip
import one_by_one
import optimal

def main():
    print(tester.tester(20, rls.heuristic))
    print(tester.tester(20, annealing.heuristic))
    #print(tester.tester(20, always_inside_mip.heuristic))
    print(tester.tester(20, one_by_one.heuristic))
    print(tester.tester(3, optimal.heuristic))

main()
