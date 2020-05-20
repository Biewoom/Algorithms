import os
import sys

def move(position, num):
    if num == 0: m = (0, 1)
    elif num == 1: m = (1, 1)
    elif num == 2: m = (1, 0)
    elif num == 3: m = (1, -1)
    elif num == 4: m = (0, -1)
    elif num == 5: m = (-1, -1)
    elif num == 6: m = (-1, 0)
    elif num == 7: m = (-1, 1)
    else: print("Imossilbe")
    return (position[0]+m[0], position[1]+m[1])

def solution(arrows):
    answer = 0
    position = (0, 0)
    vertexes = set(); edges = set()
    vertexes.add(position)
    for num in arrows:
        for i in range(2):
            edge = [position]
            position = move(position, num)
            edge.append(position)

            vertexes.add(position)
            edges.add(tuple(sorted(edge)))

    return 1 - len(vertexes) + len(edges)


if __name__ == '__main__':
    arrows = list(map(int, input().split(', ')))
    result = solution(arrows)
    print(result)
