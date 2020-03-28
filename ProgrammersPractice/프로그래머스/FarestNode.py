import os
import sys

from heapq import heappush, heappop
from collections import defaultdict

def solution(n, edges):
    INF = sys.maxsize
    hq = []; d = [INF]*n
    adj_list = defaultdict(list); ValueDict = defaultdict(int) # store value

    for edge in edges:
        v1, v2 = edge
        v1 -= 1; v2 -= 1;
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    # dijastra
    d[0] = 0; heappush(hq, (0, 0))
    while hq:
        distance, node = heappop(hq)
        for adj_node in adj_list[node]:
            if distance + 1 < d[adj_node]:
                d[adj_node] = distance + 1
                heappush(hq, (d[adj_node], adj_node))

    # print("D: ", d)
    Max = 0
    for e in d:
        Max = max(Max, e); ValueDict[e] += 1

    return ValueDict[Max]


if __name__ == '__main__':
    n = int(input())
    Loflist = []
    for i in range(7):
        v1, v2 = map(int, input().split())
        Loflist.append( [v1, v2] )
    result = solution(n, Loflist)
    print(result)
