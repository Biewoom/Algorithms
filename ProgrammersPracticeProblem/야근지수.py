import os
import sys

from bisect import insort

def solution(n, works):
    bst = []
    mid = len(works)//2
    sum = answer = 0

    for work in works:
        sum += work
        insort(bst, work*-1)

    if n >= sum: return 0

    while n > 0 and bst[0] != bst[mid]:
        minusValue = max( (n// (mid+1) ), 1)
        largestValue = bst.pop(0)*-1
        insort(bst, (largestValue - minusValue)*-1 )
        n -= minusValue

    nq, nv = divmod(n, len(bst))

    for i, Value in enumerate(bst):
        finalValue = Value*-1
        if i < nv: answer += (finalValue - nq - 1)**2
        else: answer += (finalValue - nq)**2

    return answer

if __name__ == "__main__":
    n = int(input())
    works = list(map(int, input()[1:-1].split(',')))
    result = solution(n, works)
    print(result)
