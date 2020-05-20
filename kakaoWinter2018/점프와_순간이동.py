import os
import sys

def solution(n):
    return bin(n)[2:].count('1')

if __name__ == '__main__':
    N = int(input())
    result = solution(N)
    print(result)
