import os
import sys

def makeThree(n, changer):
    if n == 0: return ""
    q, v = divmod(n, 3)
    if n % 3 == 0: return makeThree(q-1, changer) + changer[v]
    else: return makeThree(q, changer) + changer[v]

def solution(n):
    sys.setrecursionlimit(10**5)
    changer = {0: '4', 1: '1', 2: '2'}
    answer = makeThree(n, changer)
    return answer

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)
