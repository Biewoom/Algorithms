#!/bin/python3

import os
import sys

def indianJob(g, arr):

    Total = sum(arr)
    if g >= Total: return 'YES'

    Set = set()
    Set.add(0)

    while arr:
        I = arr.pop(0)
        Next_set = set()
        while Set:
            v = Set.pop()
            Next_set.add(v); Next_set.add(v + I)
        Set = Next_set

    while Set:
        a = Set.pop()
        if max(a, Total - a) <= g: return 'YES'

    return 'NO'

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        ng = input().split()

        n = int(ng[0])

        g = int(ng[1])

        arr = list(map(int, input().rstrip().split()))

        result = indianJob(g, arr)

        print(result)
