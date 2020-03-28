#!/bin/python3

import os
import sys

from heapq import heappush, heappop
from collections import defaultdict

result = 0
def find(n, P):

    if P[n] < 0: return n
    else: return find(P[n], P)

def union(x, y, P, size):

    new_size = size[x] + size[y]

    if size[x] <= size[y]:
        P[x] = y
        size[y] = new_size
    else:
        P[y] = x
        size[x] = new_size

def pre_stage(n , roads, ddict):

    # prestage disjoint set
    # kruskal's theory
    P = [-1]*n; size = [1]*n; hq = [];
    # edges list
    for road in roads:
        v1, v2, w = road
        heappush(hq, (w, v1-1, v2-1) )

    # make spanning tree
    while hq:
        w, v1, v2 = heappop(hq)
        x = find(v1, P); y = find(v2, P)
        if x != y:
            union(x,y,P,size)
            ddict[v1].append((v2, w))
            ddict[v2].append((v1, w))

def solve(c_node, p_node, adjacentdict):
    # recur from leaf to root
    global result
    childs = []; upward_w = None

    # res which come from root
    for info in adjacentdict[c_node]:
        next_node, w = info
        if next_node == p_node: upward_w = 2**w; continue
        childs.append(solve(next_node, c_node, adjacentdict))

    res = []
    acc = SUM = 0
    for child in childs:
        # cross #
        t_sum = sum(child)
        acc += SUM*len(child)
        acc += t_sum*len(res)

        res += child
        SUM += t_sum

    result += acc
    # cur_node is end
    for r in res: result += r
    #  all of these distance will go upward
    #  but not root
    if upward_w:
        for i in range(len(res)):
            res[i] += upward_w
        res.append(upward_w)

    return res

def roadsInHackerland(n, roads):
    global result
    adjacentDict = defaultdict(list)
    pre_stage(n, roads, adjacentDict)
    solve(0, -1, adjacentDict)

    return "{:b}".format(result)

if __name__ == '__main__':

    sys.setrecursionlimit(10**5)
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    result = roadsInHackerland(n, roads)

    print(result)
