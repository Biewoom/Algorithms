import os
import sys

def solution(left, right):
    n = len(left) # = len(right)
    dp = [[-1]*(n+1) for i in range(n+1)]
    dp[n][n] = 0

    for NumberOfRight in range(n, -1, -1):
        for NumberOfLeft in range(n, -1, -1):
            if dp[NumberOfRight][NumberOfLeft] == -1: continue
            if NumberOfLeft == 0 and NumberOfRight == 0: continue

            if NumberOfLeft == 0:
                dp[NumberOfRight-1][0] = max(dp[NumberOfRight-1][0], dp[NumberOfRight][0])
            elif NumberOfRight == 0:
                dp[0][NumberOfLeft-1] = max(dp[0][NumberOfLeft-1], dp[0][NumberOfLeft])
            else:
                rightCard = right[n - NumberOfRight]
                LeftCard = left[n - NumberOfLeft]

                if rightCard < LeftCard:
                    dp[NumberOfRight-1][NumberOfLeft] = max(dp[NumberOfRight-1][NumberOfLeft], dp[NumberOfRight][NumberOfLeft] + rightCard)

                # 둘 다 버리기
                dp[NumberOfRight-1][NumberOfLeft-1] = max(dp[NumberOfRight-1][NumberOfLeft-1], dp[NumberOfRight][NumberOfLeft])
                # 왼쪽만 버리기
                dp[NumberOfRight][NumberOfLeft-1] = max(dp[NumberOfRight][NumberOfLeft-1], dp[NumberOfRight][NumberOfLeft])

    return dp[0][0]

if __name__ == '__main__':
    left = list(map(int, input().split(',')))
    right = list(map(int, input().split(',')))
    result = solution(left, right)
    print(result)
