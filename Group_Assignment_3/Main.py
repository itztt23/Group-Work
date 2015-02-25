__author__ = 'Zachary'

import Group_Assignment_3.SolutionSet as SS
import math
import time
# import antigravity

def main():

    solution = []
    for i in range(0,20):
        solution.append(SS.SolutionSet())
        solution[i].load_from_no_solution_file(i)
        # solution[i].loadfromfile(i)
        # solution[i].prettyprint()

    for i in range(20):
       # print(solution[i]._array)
       start = time.clock()
       answer =  recursive(solution[i]._array, 0, len(solution[i]._array)-1)
       end = time.clock() - start
       print(len(solution[i]._array), end)

    # a = []
    #
    # correct = 0
    # for i in range(10):
    #     answer = recursive(solution[i]._array, 0, len(solution[i]._array)-1)
    #     if int(answer[0]) == int(solution[i]._solution) and int(answer[1]) == int(solution[i]._startIndex) and int(answer[2]) == int(solution[i]._endIndex):
    #         print("SOLUTIONS MATCHED")
    #         print("-------------------------------------------------------------------")
    #         correct += 1
    #         solution[i].prettyprint()
    #         print("\nOUR SOLUTION")
    #         print("Solution: ", answer[0])
    #         print("Start Index: ", answer[1])
    #         print("End Index: ", answer[2])
    #         print("Subset: ", solution[i]._array[answer[1]:answer[2]+1])
    #         print("-------------------------------------------------------------------")
    #     else:
    #         print("SOLUTIONS DID NOT MATCH: ")
    #         solution[i].prettyprint()
    #         print("\nOUR SOLUTION")
    #         print("Solution: ", answer[0])
    #         print("Start Index: ", answer[1])
    #         print("End Index: ", answer[2])
    #         print("Subset: ", solution[i]._array[answer[1]:answer[2]+1])
    #         print("-------------------------------------------------------------------")
    # print("%u/10 SOLUTIONS CORRECT" % correct)

#Takes three tuples in the form (value, index, index)
#Returns the tuple with the smallest absolute value
def min_abs_value(a1, a2, a3):
    best = (float('inf'), 0, 0)
    if abs(a1[0]) < abs(best[0]):
        best = a1
    if abs(a2[0]) < abs(best[0]):
        best = a2
    if abs(a3[0]) < abs(best[0]):
        best = a3
    return best

def make_suffix(A):
    array = []
    for i in range(len(A)):
        #summation of everything up to A[i]
        array.append(sum(A[0:i+1]))
    return array

def make_prefix(A):
    array = []
    for i in range(len(A)):
        #summation of everything up to A[i]
        array.insert(0, sum(A[len(A)-i-1:len(A)]))
    return array

def methodTwo(prefix, suffix):
    if(len(prefix) is 0 or len(suffix) is 0):
        return (float('inf'), None, None)

    bestValue = float('inf')
    prefixIndex = -1
    suffixIndex = -1

    for value in prefix:
        current = findClosestSumToZero(suffix, 0, len(suffix)-1, value)
        if abs(current + value) < abs(bestValue):
            prefixIndex = prefix.index(value)
            suffixIndex = suffix.index(current)
            bestValue = abs(current + value)
    return(bestValue, prefix[prefixIndex], suffix[suffixIndex])

#Requires A to be sorted
def findClosestSumToZero(A, low, high, k):
    find = -1 * k
    if high - low == 1:
        if abs(A[low] + k) > abs(A[high] + k):
            return A[high]
        else:
            return A[low]
    if high - low == 0:
        return A[high]
    else:
        mid = int(math.floor((high + low)/2))
        if A[mid] == find:
            return A[mid]
        elif A[mid] < find:
            return findClosestSumToZero(A, mid, high, k)
        elif A[mid] > find:
            return findClosestSumToZero(A, low, mid, k)


def recursive(A, start, end):
    mid = int((start+end)/2)
    if start == mid or end == mid:
        return (A[start], start, start)
    else:
        firstHalf = A[start:mid]
        secondHalf = A[mid:end]

        prefix = make_prefix(firstHalf)
        suffix = make_suffix(secondHalf)

        prefixS = sorted(prefix)
        suffixS = sorted(suffix)

        methodTwoReturn = methodTwo(prefixS, suffixS)         #(value, value in prefix, value in suffix)

        if(methodTwoReturn[1] is not None):
            prefixIndex = prefix.index(methodTwoReturn[1])
            suffixIndex = suffix.index(methodTwoReturn[2])
            startIndex = start + prefixIndex
            endIndex = mid + suffixIndex
            methodTwoReturn = (methodTwoReturn[0], startIndex, endIndex)

        return min_abs_value(recursive(A, start, mid), recursive(A, mid, end), methodTwoReturn)


if __name__ == "__main__":
    main()