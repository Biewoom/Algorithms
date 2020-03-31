import os
import sys

def check(x, y, state, board):
    # state 0: horizontal, 1: vertical
    if state == 0:
        if x < 0 or x >= len(board): return False
        elif y - 1 < 0 or y >= len(board): return False
        elif board[x][y] == 1 or board[x][y-1] == 1: return False
        else: return True

    else: #state == 1
        if x - 1 < 0 or x >= len(board): return False
        elif y < 0 or y >= len(board): return False
        elif board[x-1][y] == 1 or board[x][y] == 1: return False
        else: return True

def solution(board):

    INF = sys.maxsize
    dp = [ [[INF]*len(board) for i in range(len(board))] for i in range(2) ]
    Q = [(0, 1, 0)]; time = 0
    while True:
        next_Q = []
        while Q:
            x, y, state = Q.pop(0)
            if not check(x,y,state,board): continue
            if dp[state][x][y] <= time: continue
            if x == len(board)-1 and y == len(board)-1: return time
            dp[state][x][y] = time
            # move 4 directions
            next_Q.append((x, y+1, state))
            next_Q.append((x, y-1, state))
            next_Q.append((x+1, y, state))
            next_Q.append((x-1, y, state))
            # rotate
            if state == 0:
                if x+1 < len(board) and board[x+1][y] == 0 and board[x+1][y-1] == 0:
                    next_Q.append((x+1, y-1, 1)); next_Q.append((x+1, y, 1))

                if x-1 > 0 and board[x-1][y] == 0 and board[x-1][y-1] == 0:
                    next_Q.append((x, y-1, 1)); next_Q.append((x, y, 1))

            else: #state == 1:
                if y+1 < len(board) and board[x][y+1] == 0 and board[x-1][y+1] == 0:
                    next_Q.append((x, y+1, 0)); next_Q.append((x-1, y+1, 0))
                if y-1 > 0 and board[x-1][y-1] == 0 and board[x][y-1] == 0:
                    next_Q.append((x, y, 0)); next_Q.append((x-1, y, 0))
        time += 1
        Q = next_Q

if __name__ == '__main__':
    board = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        board.append(list(map(int, line.split())))
    result = solution(board)
    print(result)
