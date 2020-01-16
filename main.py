import tester
import rls
import annealing

def main():
    print(tester.tester(100, rls.heuristic))
    print(tester.tester(100, annealing.heuristic))

main()
