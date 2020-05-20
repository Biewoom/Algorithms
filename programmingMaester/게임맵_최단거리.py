
import os
import sys

from collections import defaultdict

def solution(maps):
    n = len(maps); m = len(maps[0])
    edgeHashMap = defaultdict(list); distanceHashMap = {}

    for r in range(n):
        for c in range(m):
            fromID = r*m + c
            if maps[r][c] == 0: continue
            else:
                moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for move in moves:
                    nextR, nextC = r+move[0], c+move[1]
                    if 0 <= nextR < n and 0 <= nextC < m and maps[nextR][nextC] == 1:
                        toID = nextR*m + nextC
                        edgeHashMap[fromID].append(toID)

    destination = (n-1)*m + (m-1)
    if destination not in edgeHashMap: return -1

    for node in edgeHashMap: distanceHashMap[node] = sys.maxsize

    # virtualStart
    distanceHashMap[-1] = 0
    routes = [(-1, 0)]

    while routes:
        fromNode, toNode = routes.pop(0)
        if distanceHashMap[fromNode] + 1 >= distanceHashMap[toNode]: continue
        distanceHashMap[toNode] = distanceHashMap[fromNode] + 1

        for nextNode in edgeHashMap[toNode]:
            routes.append((toNode, nextNode))

    return distanceHashMap[destination] if distanceHashMap[destination] != sys.maxsize else -1

if __name__ == '__main__':
    lines = input()[1:-1].split('],[')
    maps = []
    for line in lines:
        maps.append(list(map(int, line.split(','))))

    result = solution(maps)
    print(result)
