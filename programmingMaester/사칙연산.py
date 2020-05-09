import os
import sys

dp = {}

def solve(startIndex, endIndex, arr, preBit):
    global dp
    # 1: 앞이 +, 0: 앞이 -
    if startIndex == endIndex: return 0
    if (startIndex, endIndex, preBit) in dp:
        return dp[(startIndex, endIndex, preBit)]

    curBit = 0 if arr[startIndex] == '-' else 1
    if curBit:
         result = int( arr[startIndex+1] ) + solve(startIndex+2, endIndex, arr, preBit)
         dp[(startIndex, endIndex, preBit)] = result
         return result
    else:
        newEnd = endIndex
        Max = sys.maxsize*-1; Min = sys.maxsize
        while startIndex + 2 <= newEnd:
            value = (int(arr[startIndex+1]) + solve(startIndex+2, newEnd, arr, preBit^1) )*-1 + solve(newEnd, endIndex, arr, preBit)
            Max = max(Max, value)
            Min = min(Min, value)
            newEnd -= 2

        if preBit:
            dp[(startIndex, endIndex, preBit)] = Max
            return Max
        else:
            dp[(startIndex, endIndex, preBit)] = Min
            return Min

def solution(arr):
    headInt = int(arr[0])
    leftArr = arr[1:]
    answer = headInt + solve(0, len(leftArr), leftArr, 1)
    return answer

if __name__ == '__main__':
    arr = input()[1:-1].split('","')
    result = solution(arr)
    print(result)
