import os
import sys

from collections import defaultdict
from heapq import heappush, heappop

def find(a, P):
    if P[a] == a: return a
    else: return find(P[a], P)

def union_find(a, b, P, depth):
    x = find(a, P)
    y = find(b, P)
    if x != y:
        if depth[x] <= depth[y]:
            depth[y] = max(depth[y], depth[x]+1)
            P[x] = y
        else:
            depth[x] = max(depth[x], depth[y]+1)
            P[y] = x

def move1(r, c, P, depth, land, height):
    n = len(land); cur = land[r][c]
    URDL = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for _move in URDL:
        moveR = r + _move[0]; moveC = c + _move[1]
        if  0 <= moveR < n and 0 <= moveC < n:
            if abs(cur - land[moveR][moveC]) <= height:
                index1 = n*r + c; index2 = n*moveR + moveC
                union_find(index1, index2, P, depth)

def move2(r, c, n, matrix, edgehq):
    cur = matrix[r][c]
    URDL = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for _move in URDL:
        moveR = r + _move[0]; moveC = c + _move[1]
        if  0 <= moveR < n and 0 <= moveC < n:
            moveH, moveG = matrix[moveR][moveC]
            if moveG != cur[1]:
                heappush( edgehq, ((abs(cur[0]-moveH), cur[1], moveG)) )

def makeNewMatrix(newMatrix, n, P, land):
    for r in range(n):
        row = []
        for c in range(n):
            index = n*r + c
            group = find(index, P)
            row.append ( (land[r][c], group) )
        newMatrix.append(row)

def solution(land, height):
    sys.setrecursionlimit(10**5)
    n = len(land)
    P = [i for i in range(0, n*n)]; depth = [1]*(n*n)

    for r in range(n):
        for c in range(n):
            move1(r, c, P, depth, land, height)

    newMatrix = []
    makeNewMatrix(newMatrix, n, P, land)

    # kruskal-algorithm
    pHashMap = {}
    depthHashMap = {}
    edgehq = []

    for r in range(n):
        for c in range(n):
            group = newMatrix[r][c][1]
            pHashMap[group] = group; depthHashMap[group] = 1
            move2(r, c, n, newMatrix, edgehq)

    result = 0
    while edgehq:
        distance, v1, v2 = heappop(edgehq)
        x = find(v1, pHashMap); y = find(v2, pHashMap)
        if x != y:
            union_find(x, y, pHashMap, depthHashMap)
            result += distance

    return result


if __name__ == '__main__':
    height = int(input())
    land = []
    lines = input()[1:-1].split('], [')
    for line in lines:
        land.append(list(map(int, line.split(', ') ) ) )

    result = solution(land, height)
    print( result )
