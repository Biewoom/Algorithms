import os
import sys

def solution(n):
    if n == 1: return 0
    elif n == 2: return 2
    elif n == 3: return 3
    else:
        pre1 = 2; pre2 = 3; M = 1000000007
        for i in range(n-3):
            temp = pre1+pre2
            pre1, pre2 = pre2, temp

        return pre2%M

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)
