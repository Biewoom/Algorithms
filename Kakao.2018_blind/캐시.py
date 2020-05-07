import os
import sys

def solution(cacheSize, cities):
    answer = 0
    LRU = []
    for city in cities:
        Hit = False
        for i in range(0, len(LRU)):
            if LRU[i].lower() == city.lower():
                Hit = True; break
        if Hit:
            answer += 1
            LRU.pop(i); LRU.append(city)
        else:
            answer += 5
            if cacheSize == 0: continue
            if len(LRU) >= cacheSize:
                LRU.pop(0)
            LRU.append(city)
    return answer

if __name__ == '__main__':
    cacheSize = int(input())
    lines = input().split(',')
    cities = []
    for line in lines:
        cities.append(line[1:-1])

    result = solution(cacheSize, cities)
    print(result)
