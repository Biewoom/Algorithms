import os
import sys

result = 0

def check(column, row, dp):

    for cmpR in range(0, row):
        cmpC = dp[cmpR]
        if cmpC == column: return False
        if abs(cmpR - row) == abs(cmpC-column): return False

    return True

def makeQueen(n, row, dp):
    global result

    if row == n: result += 1; return
    else:
        for c in range(0, n):
            if check(c, row, dp):
                dp[row] = c
                makeQueen(n, row+1, dp)

def solution(n):
    global result
    dp = [0]*n
    makeQueen(n, 0, dp)
    return result

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)
