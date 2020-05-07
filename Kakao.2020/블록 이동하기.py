import os
import sys
from collections import defaultdict

# style|axis|direciton
ValueArray = [[[None]*2 for i in range(2)] for i in range(2)]
CheckArray = [[[None]*2 for i in range(2)] for i in range(2)]

def check(coord1, coord2, board):
    x1, y1 = coord1; x2, y2 = coord2
    if min(x1, y1, x2, y2) < 0: return False
    elif max(x1, y1, x2, y2) >= len(board): return False
    elif board[x1][y1] == 1 or board[x2][y2] == 1: return False
    else: return True

def goNEWS(coord1, coord2, i):
    move = [(-1,0), (0, 1), (0, -1), (1,0)]
    new_coord1 = (coord1[0]+move[i][0], coord1[1]+move[i][1]); new_coord2 = (coord2[0]+move[i][0], coord2[1]+move[i][1])
    return sorted((new_coord1, new_coord2))

def rotate(coord1, coord2, board, axis, direction):
    global ValueArray, CheckArray

    axis_coord = coord1 if axis == 0 else coord2
    style = 0 if coord2[1] > coord1[1] else 1

    Check = CheckArray[style][axis][direction]
    Value = ValueArray[style][axis][direction]
    Check_coord = (axis_coord[0] + Check[0], axis_coord[1]+Check[1])
    new_coord = (axis_coord[0]+Value[0], axis_coord[1]+Value[1])

    if 0 <= Check_coord[0] < len(board) and 0 <= Check_coord[1] < len(board) and board[Check_coord[0]][Check_coord[1]] == 0:
        return sorted( (new_coord, axis_coord) )
    else:
        return ((-1,-1), (-1,-1))

def initialize(ValueArray, CheckArray):
    CheckArray[0][0][0] = (-1,1);   ValueArray[0][0][0] = (-1,0)
    CheckArray[0][0][1] = (1,1);    ValueArray[0][0][1] = (1,0)
    CheckArray[0][1][0] = (-1,-1);  ValueArray[0][1][0] = (-1,0)
    CheckArray[0][1][1] = (1,-1);   ValueArray[0][1][1] = (1,0)
    CheckArray[1][0][0] = (1,1);    ValueArray[1][0][0] = (0,1)
    CheckArray[1][0][1] = (1,-1);   ValueArray[1][0][1] = (0,-1)
    CheckArray[1][1][0] = (-1,1);   ValueArray[1][1][0] = (0,1)
    CheckArray[1][1][1] = (-1,-1);  ValueArray[1][1][1] = (0,-1)

def solution(board):
    global ValueArray, CheckArray
    initialize(ValueArray, CheckArray)
    HashMap = defaultdict(int)
    Q = [( (0, 0), (0, 1) )]
    time = 0

    while True:
        next_Q = []
        while Q:
            coord1, coord2 = Q.pop(0)
            if not check(coord1, coord2, board): continue
            if (coord1, coord2) in HashMap and HashMap[(coord1, coord2)] <= time: continue
            if coord2[0] == len(board)-1 and coord2[1] == len(board)-1: return time
            HashMap[(coord1, coord2)] = time

            for i in range(4):
                next_Q.append(tuple(goNEWS(coord1, coord2, i)))

            for axis in range(2):
                for direction in range(2):
                    next_Q.append(tuple(rotate(coord1, coord2, board, axis, direction)))

        time += 1
        Q = next_Q

if __name__ == '__main__':
    board = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        board.append(list(map(int, line.split())))
    result = solution(board)
    print(result)
