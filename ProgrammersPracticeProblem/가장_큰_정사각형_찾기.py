import os
import sys

def solution(board):
    dpBoard = board.copy()
    Max = 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j]:
                dpBoard[i][j] = min(dpBoard[i-1][j-1], dpBoard[i-1][j], dpBoard[i][j-1]) + 1
                Max = max(Max, dpBoard[i][j])
                
    return Max**2


if __name__ == '__main__':
    board = []
    lines = input()[1:-1].split('],[')
    for line in lines:
        board.append(list(map(int, line.split(','))))

    result = solution(board)
    print(result)
