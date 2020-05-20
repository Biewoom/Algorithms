import os
import sys

def check(time, n, cores):

    work = n
    for core in cores:
        work -= (time//core) + 1
        if work <= 0: return True
        
    return False

def solution(n, cores):
    Max = 500000000
    Min = 0
    if n < len(cores): return n

    while Min < Max:
        mid = (Min+Max)//2
        if check(mid, n, cores): Max = mid
        else: Min = mid+1

    Time = Min
    answer = []
    leftWork = n
    for idx, core in enumerate(cores):
        leftWork -= ( (Time-1)//core + 1 )
        if Time%core == 0: answer.append(idx+1)

    return answer[leftWork-1]

if __name__ == '__main__':
    n = int(input())
    cores = list(map(int, input().split(',')))
    result = solution(n, cores)
    print(result)
