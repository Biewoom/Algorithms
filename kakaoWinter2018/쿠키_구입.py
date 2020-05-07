import os
import sys

def findSum(cookie, sumMaxtrix):
    for start in range(0, len(cookie)):
        for end in range(start, len(cookie)):
            sumMaxtrix[start][end+1] = sumMaxtrix[start][end] + cookie[end]

def solution(cookie):
    sumMatrix = [[0]*(len(cookie)+1) for i in range(len(cookie))]
    findSum(cookie, sumMatrix)
    Max = 0
    for m in range(0, len(cookie)-1):

        leftSet = set()
        for i in range(0, m+2):
            leftSet.add(sumMatrix[i][m+1])

        for j in range(m+2, len(cookie)+1):
            rightSum = sumMatrix[m+1][j]
            if rightSum in leftSet:
                Max = max(Max, rightSum)

    return Max

if __name__ == '__main__':
    cookie = list(map(int, input().split(',')))
    result = solution(cookie)
    print(result)
