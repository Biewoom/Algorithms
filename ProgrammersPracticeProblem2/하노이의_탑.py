import os
import sys

def hanoi(n, startBar, helperBar, endBar, answer):
    if n == 0: return

    hanoi(n-1, startBar, endBar, helperBar, answer)
    answer.append( [startBar, endBar] )
    hanoi(n-1, helperBar, startBar, endBar, answer)

def solution(n):
    sys.setrecursionlimit(10**5)
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)
