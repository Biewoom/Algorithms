import os
import sys
from heapq import heappush, heappop

def solution(food_times, k):
    hq = []
    turn_stack = 0; pre_k = last_omit = None

    for i in range(len(food_times)):
        heappush(hq, [food_times[i], i+1] )

    while hq and k >= 0:
        omit = heappop(hq)
        pre_k = k
        turns = omit[0] - turn_stack
        k -= (len(hq)+1) * turnsn
        turn_stack += turns
        last_omit = omit[1]

    if k < 0:
        left_foods = sorted( [x[1] for x in hq] + [last_omit] )
        move = pre_k % len(left_foods)
        return left_foods[move]

    else: return -1


if __name__ == '__main__':
    k = int(input())
    food_times = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        food_times.append(int(line))
    result = solution(food_times, k)
    print(result)
