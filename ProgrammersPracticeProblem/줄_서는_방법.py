import os
import sys

def factorialDP(dp):
    dp[0] = dp[1] = 1
    for i in range(2, 20):
        dp[i] = dp[i-1]*i

def solve(arr, k, factorial, answer):
    if len(arr) <= 0: return

    divider = factorial[len(arr)-1]
    n, q = divmod(k-1, divider)

    answer.append(arr.pop(n))
    solve(arr, q+1, factorial, answer)


def solution(n, k):
    answer = []; dp = [0]*20
    factorialDP(dp)
    arr = [x for x in range(1, n+1)]
    solve(arr, k, dp, answer)

    return answer

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    result = solution(n, k)
    print(result)
