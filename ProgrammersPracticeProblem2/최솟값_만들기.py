import os
import sys

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)

    for a, b in zip(A, B): answer += a*b

    return answer

if __name__ == '__main__':
    A = list(map(int, input().split(',')))
    B = list(map(int, input().split(',')))
    result = solution(A,B)
    print(result)
