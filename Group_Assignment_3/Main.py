__author__ = 'Zachary'

import Group_Assignment_3.SolutionSet as SS
import Group_Assignment_3.methodTwo as MT

def main():
    solution = []
    for i in range(0,10):
        solution.append(SS.SolutionSet())
        solution[i].loadfromfile(i)

    for i in range (0,10):
        print(algorithm(solution[i]._array))


def algorithm(A):
    a = len(A)
    if a is 1:
        return A[0]
    else:
        return min(algorithm(A[0:int(a/2)]), algorithm(A[int(a/2):a]), MT.methodTwo(A[0:int(a/2)], A[int(a/2):a])[0])



if __name__ == "__main__":
    main()