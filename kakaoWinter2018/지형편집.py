import os
import sys
from collections import defaultdict

def solve(standard, heights, P, Q)->int:
    sum = 0
    for h in heights:
        if standard >= h: sum += (standard-h)*P*heights[h]
        else: sum += (h - standard)*Q*heights[h]
    return sum

def solution(land, P, Q):
    heights = defaultdict(int); flatten = []

    for r in range(len(land)):
        for c in range(len(land[0])):
            heights[land[r][c]] += 1
            flatten.append(land[r][c])

    flatten.sort()
    minimum_index = (len(flatten)*Q) // (Q+P)
    answer = solve(flatten[minimum_index], heights, P, Q)
    return answer


if __name__ == '__main__':
    lines = input()[1:-1].split('],[')
    P = int(input())
    Q = int(input())
    land = []
    for line in lines:
        land.append(list(map(int, line.split(',')) ) )

    result = solution(land, P, Q)
    print(result)
