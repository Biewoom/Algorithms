import os
import sys


def solution(land):
    DP = [0]*4

    for i in range(4): DP[i] = land[0][i]

    for row in range(1, len(land)):
        nextDP = [0]*4

        for i in range(4):
            Max = 0
            for j in range(4):
                if i == j: continue
                Max = max(Max, DP[j])

            nextDP[i] += (Max + land[row][i])
        DP = nextDP

    return max(DP)


if __name__ == '__main__':
    land = []
    lines = input()[1:-1].split('],[')
    for line in lines:
        land.append(list(map(int, line.split(','))))

    result = solution(land)
    print(result)
