import os
import sys

def solution(d, budget):
    answer = 0
    d.sort()
    while d and budget - d[0] >= 0:
        budget -= d[0]
        answer += 1
        d.pop(0)

    return answer

if __name__ == '__main__':
    budget = int(input())
    d = list( map(int, input().split(',') ) )
    result = solution(d, budget)
    print(result)
