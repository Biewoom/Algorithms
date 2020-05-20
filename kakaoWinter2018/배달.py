import os
import sys

def solution(N, road, K):
    # floyd-marshall
    answer = 0
    lengthMatrix = [[sys.maxsize]*N for i in range(N)]

    for zeroMaker in range(N):
        lengthMatrix[zeroMaker][zeroMaker] = 0

    for r in road:
        node1, node2, length = r
        node1 -= 1; node2 -= 1
        lengthMatrix[node1][node2] = min(lengthMatrix[node1][node2], length)
        lengthMatrix[node2][node1] = min(lengthMatrix[node2][node1], length)

    for interNode in range(0, N):
        for node1 in range(0, N):
            if node1 == interNode: continue

            for node2 in range(0, N):
                lengthMatrix[node1][node2] = min(lengthMatrix[node1][node2], lengthMatrix[node1][interNode] + lengthMatrix[interNode][node2])

    for node in range(0, N):
        if lengthMatrix[0][node] <= K: answer += 1

    return answer


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    road = []
    lines = input()[1:-1].split('],[')
    for line in lines:
        road.append( list(map(int, line.split(',') ) ) )

    result = solution(N, road, K)
    print(result)
