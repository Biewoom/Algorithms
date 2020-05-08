import os
import sys
from math import ceil


def gcd(a, b):
    if a == 0: return b
    else: return gcd(b%a, a)

def solution(w,h):
    small, big = sorted([w, h])
    sum = small*big
    _gcd = gcd(small, big)
    return sum - _gcd*( (small//_gcd) + (big//_gcd) - 1 )

if __name__ == '__main__':
    w = int(input())
    h = int(input())
    result = solution(w, h)
    print(result)
