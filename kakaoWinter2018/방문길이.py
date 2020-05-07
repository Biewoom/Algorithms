import os
import sys

def solution(dirs):
    paths = set()
    Position = (0, 0)
    for dir in dirs:
        if dir == 'U': newPosition = (Position[0] + 1, Position[1] )
        elif dir == 'L': newPosition = (Position[0], Position[1] - 1)
        elif dir == 'R': newPosition = (Position[0], Position[1] + 1)
        elif dir == 'D': newPosition = (Position[0] - 1, Position[1])
        else: print("Impossible")

        if -5 <= newPosition[0] <= 5 and -5 <= newPosition[1] <= 5:
            path = sorted( [Position, newPosition] )
            paths.add(tuple(path))
            Position = newPosition

    return len(paths)

if __name__ == '__main__':
    dirs = input()
    result = solution(dirs)
    print(result)
