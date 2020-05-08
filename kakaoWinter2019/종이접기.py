import os
import sys

def numToString(length, num):
    _str = "{:0%db}"%length
    return _str.format(num)

def reverse(length, num)->str:
    compareNum = (1 << length) - 1
    compareNum ^= num
    return numToString(length, compareNum)[::-1]

def solve(length, cur):
    curStr = numToString(length, cur)
    reverseStr = reverse(length, cur)
    nextStr = curStr + '0' + reverseStr
    return 2*length+1, int(nextStr, 2)

def solution(n):
    if n == 1: return [0]
    elif n == 2: return [0, 0, 1]
    else:
        length = 3; cur = 1
        for i in range(n-2):
            nextLength, nextCur = solve(length, cur)

            length = nextLength
            cur = nextCur
        return list(map(int, numToString(length, cur) ) )

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)
