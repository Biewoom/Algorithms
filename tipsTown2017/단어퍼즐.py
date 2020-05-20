import os
import sys

def solution(strs, t):
    global result

    dp = [sys.maxsize]*len(t)
    dp += [0]*6
    strSet = set(strs)

    # print("dp: ", dp)
    # print("strSet: ", strSet)

    for i in range(len(t)-1, -1, -1):
        for k in range(1, 6):
            if t[i:i+k] in strSet:
                dp[i] = min(dp[i], dp[i+k] +1)

    return dp[0] if dp[0] != sys.maxsize else -1


if __name__ == '__main__':
    strs = input()[1:-1].split('","')
    t = input()[1:-1]
    result = solution(strs, t)
    print(result)
