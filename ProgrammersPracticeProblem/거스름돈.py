import os
import sys

def solution(n, money):
    M = 1000000007
    DP = [[0]*(n+1) for i in range(len(money)+1)]
    DP[0][0] = 1

    for j in range(1, len(money)+1):
        for num in range(0, n+1):
            DP[j][num] += DP[j-1][num]%M
            if num >= money[j-1]:
                DP[j][num] += DP[j][num-money[j-1]]%M

    return DP[len(money)][n] % M

if __name__ == '__main__':
    n = int(input())
    money = list(map(int, input()[1:-1].split(',')))
    result = solution(n, money)
    print(result)
