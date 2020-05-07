import os
import sys

def numberSystem(number, base):
    notation = '0123456789ABCDEF'
    q, r = divmod(number, base)
    n = notation[r]
    return numberSystem(q, base) + n if q else notation[r]

def solution(n, t, m, p):
    result = ""; number= turn = 0; base = n
    while len(result) < t:
        curNumber = numberSystem(number, base)
        while len(result) < t and curNumber:
            echo = curNumber[0]
            if turn+1 == p: result += echo
            turn += 1; turn %= m
            curNumber = curNumber[1:]
        number += 1
    return result

if __name__ == '__main__':
    n = int(input())
    t = int(input())
    m = int(input())
    p = int(input())

    result = solution(n, t, m, p)
    print(result)
