import os
import sys
from math import sqrt

def solution(begin, end):
    answer = []

    for num in range(begin, end+1):
        if num == 1: answer.append(0); continue
        for n in range(2, int(sqrt(num))+1):
            if num%n == 0 and num//n <= 10000000:
                answer.append(num//n)
                break
        else:
            answer.append(1)

    return answer

if __name__ == '__main__':
    begin = int(input())
    end = int(input())
    result = solution(begin, end)
    print(result)
