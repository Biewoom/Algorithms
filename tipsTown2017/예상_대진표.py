import os
import sys

from math import ceil

def solution(n,a,b):
    answer = 1

    while ceil(a/2) != ceil(b/2):
        answer += 1
        a = ceil(a/2); b = ceil(b/2)

    return answer

if __name__ == '__main__':
    n = int(input())
    a = int(input())
    b = int(input())
    result = solution(n, a, b)
    print(result)
