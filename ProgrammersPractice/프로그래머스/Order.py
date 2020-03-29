import sys
import os


def solve(n, Loflist):
    Unknown = 'Unknown'
    dp = [[Unknown]*n for i in range(n)]

    # evaluate myself
    for i in range(n):
        dp[i][i] = 0

    for l in Loflist:
        v1, v2 = l
        v1 -= 1; v2 -= 1
        dp[v1][v2] = 1 # win
        dp[v2][v1] = -1 # lose

    # floyd-warsell

    for k in range(n): # intermediate node
        for i in range(n):
            for j in range(n):
                if i == k: continue
                if dp[i][k] == 1 and dp[k][j] == 1: dp[i][j] = 1
                if dp[i][k] == -1 and dp[k][j] == -1: dp[i][j] = -1
                else: continue

    # count
    ans = 0
    for i in range(n):
        Found = False
        for j in range(n):
            if dp[i][j] == Unknown: Found = True

        if not Found:
            ans += 1

    return ans

if __name__ == '__main__':
    n = int(input())
    Loflist = []
    for line in sys.stdin:
        if line == '': break
        Loflist.append( list( map(int, line.split()) ) )

    result = solve(n, Loflist)
    print(result)
