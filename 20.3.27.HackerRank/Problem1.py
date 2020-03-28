import os
import sys
import re
import unittest

# Enter your code here. Read input from STDIN. Print output to STDOUT


def solve(n, c, m):

    res = wrappers = n//c

    while wrappers >= m:
        wrappers -= m
        res += 1; wrappers += 1

    return res

if __name__ == '__main__':
    t = int(input())
    for iter_t in range(t):
        n, c, m = map(int, input().split())
        print(solve(n,c,m))
