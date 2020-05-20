import os
import sys

from bisect import bisect_right, insort
from heapq import heappush, heappop

def solution(A, B):

    answer = 0; hq = []; bst = []

    for a in A: heappush(hq, a*-1)
    for b in B: insort(bst, b)

    while hq:
        numA = heappop(hq)*-1
        index = bisect_right(bst, numA)

        if index >= len(bst): bst.pop(0)
        else:
            bst.pop(index)
            answer += 1

    return answer

if __name__ == '__main__':
    A = list(map(int, input().split(',')))
    B = list(map(int, input().split(',')))
    result = solution(A, B)
    print(result)
