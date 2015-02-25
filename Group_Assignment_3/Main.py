__author__ = 'Zachary'

import Group_Assignment_3.SolutionSet as SS
import Group_Assignment_3.methodTwo as MT
# import antigravity

def main():
    solution = []
    for i in range(0,10):
        solution.append(SS.SolutionSet())
        solution[i].loadfromfile(i)

    solution[1].prettyprint()

    # for i in range (0,10):
    #     print(algorithm(solution[i]._array))

    print(algorithm(solution[1]._array, solution[1]._array))

def closesttozero(a1, a2, a3):
    best = (float('inf'), 0, 0)
    if abs(a1[0]) < abs(best[0]):
        best = a1
    if abs(a2[0]) < abs(best[0]):
        best = a2
    if abs(a3[0]) < abs(best[0]):
        best = a3
    return best

def makeprefix(A):
    array = []
    for i in range(len(A)):
        #summation of everything up to A[i]
        array.append(sum(A[0:i+1]))
    return array

def makesuffix(A):
    array = []
    for i in range(len(A)):
        #summation of everything up to A[i]
        array.insert(0, sum(A[len(A)-i-1:len(A)]))
    return array

def algorithm(A, original):
    a = len(A)
    if a is 1:
        return (A[0], original.index(A[0]), original.index(A[0]))
    else:
        prefix = makeprefix(A[0:int(a/2)])
        suffix = makesuffix(A[int(a/2):a])

        prefix = sorted(prefix)
        suffix = sorted(suffix)

        return closesttozero(algorithm(A[0:int(a/2)], original), algorithm(A[int(a/2):a], original), MT.methodTwo(prefix, suffix))


if __name__ == "__main__":
    main()