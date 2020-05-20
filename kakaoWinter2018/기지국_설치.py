import os
import sys

def findMaxStations(town, w):
    cover = 2*w + 1
    q, m = divmod(town, cover)
    if m == 0: return q
    else: return q+1

def solution(n, stations, w):
    if len(stations) == 0: return findMaxStations(n)

    answer = 0
    towns = []

    stations.sort()
    start = stations[0] - w - 1
    end = stations[0] + w - 1

    if start <= 0: pass
    else: towns.append(start)

    for station in stations[1:]:
        station -= 1
        curStart = station - w
        curEnd = station + w

        if curStart <= end:
            start = start; end = curEnd
        else:
            towns.append(curStart - end - 1)
            start = curStart; end = curEnd

    if end >= n-1: pass
    else: towns.append(n-1 - end)


    for town in towns:
        answer += findMaxStations(town, w)

    return answer

if __name__ == '__main__':
    n = int(input())
    w = int(input())
    stations = list(map(int, input().split(',')))
    result = solution(n, stations, w)
    print(result)
