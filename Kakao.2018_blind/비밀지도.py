import os
import sys

def solution(n, arr1, arr2):
    _str = "{:0%db}"%n
    answer = []
    for a1, a2 in zip(arr1, arr2):
        ar = a1|a2; comBinary = _str.format(ar)
        arr = ""
        for chr in comBinary:
            if chr == '1': arr += "#"
            else: arr += " "
        answer.append(arr)

    return answer

if __name__ == '__main__':
    n = int(input())
    arr1 = list(map(int, input().split(',') ) )
    arr2 = list(map(int, input().split(',') ) )
    result = solution(n, arr1, arr2)
    print(result)
