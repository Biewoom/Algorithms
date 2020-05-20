import os
import sys


def solution(n):
    if n == 1: return 1
    elif n == 2: return 2
    else:
        v1 = 1; v2 = 2

        for i in range(0, n-2):
            temp = v1 + v2
            v1, v2 = v2, temp

    return v2%1234567

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)
