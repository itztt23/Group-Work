__author__ = 'Zachary'

import math

def methodTwo(prefix, suffix):
    bestValue = float('inf')
    prefixIndex = -1
    suffixIndex = -1

    for value in prefix:
        current = findClosestSumToZero(suffix, 0, len(suffix)-1, value)
        if abs(current) < abs(bestValue):
            prefixIndex = prefix.index(value)
            suffixIndex = suffix.index(current)
            bestValue = abs(current + value)
    return(bestValue, prefixIndex, suffixIndex)

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
        if A[mid] < find:
            return findClosestSumToZero(A, mid, high, k)
        elif A[mid] > find:
            return findClosestSumToZero(A, low, mid, k)
        elif A[mid] == find:
            return A[mid]