import os
import sys


def Counterclockwise(matrix):
    new_matrix = [[0]*len(matrix) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[len(matrix)- 1 - j][i] = matrix[i][j]
    return new_matrix

def solution(keys, locks):
    # four direction
    # counter clockWise
    m = len(keys); n = len(locks); lock_x = lock_y = m-1
    options = [0, 90, 180, 270]

    for op in options:
        if op != 0: keys = Counterclockwise(keys)
        print("keys: ", keys)
        for i in range(0, m+n):
            for j in range(0, m+n):
                VirtualMatrix = [[None]*(n+2*m) for i in range((n+2*m))]
                key_x = i; key_y = j

                for x in range(0, m):
                    for y in range(0, m):
                        VirtualMatrix[key_x+x][key_y+y] = keys[x][y]

                Unlock = True
                for z in range(0, n):
                    for k in range(0, n):
                        if VirtualMatrix[lock_x+z][lock_y+k] is None:
                            if locks[z][k] == 0: Unlock = False
                            else: continue
                        else:
                            if VirtualMatrix[lock_x+z][lock_y+k]^locks[z][k] != 1: Unlock = False
                            else: continue

                if Unlock: return True

    return False


if __name__ == '__main__':
    k = int(input())
    keys = []; locks = []
    for i in range(k):
        keys.append(list(map(int, input().split())))
    l = int(input())
    for i in range(l):
        locks.append(list(map(int, input().split())))

    result = solution(keys, locks)
    print(result)
