import os
import sys

from math import sqrt

def formular(a, n):
    b = 1 - 2*a
    c = 4*(a**2) - (4*a) + 1 + (8*n)
    return (b + sqrt(c)) / 2

def validCheck(a, n):
    result = formular(a, n)
    if result != int(result): return False
    if result > (n - a + 1): return False
    return True

def solution(n):
    answer = 0

    for num in range(1, n+1):
        if validCheck(num, n):
            answer += 1

    return answer

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)
