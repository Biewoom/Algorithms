import os
import sys

def makeD(matrix_sizes, d):
    for i, matrix in enumerate(matrix_sizes):
        d[i] = matrix[0]
    d[-1] = matrix_sizes[-1][1]

def solution(matrix_sizes):
    d = [0]*(len(matrix_sizes)+1)
    dp = [[sys.maxsize]*len(matrix_sizes) for i in range(len(matrix_sizes))]
    makeD(matrix_sizes, d)

    for i in range(len(matrix_sizes)):
        for j in range(len(matrix_sizes)):
            x, y = j, i+j
            if y >= len(matrix_sizes): continue
            if x == y: dp[x][y] = 0; continue

            for k in range(x, y):
                dp[x][y] = min(dp[x][y], dp[x][k] + dp[k+1][y] + d[x]*d[k+1]*d[y+1])

    return dp[0][len(matrix_sizes)-1]

if __name__ == '__main__':
    matrix_sizes = []
    lines = input()[1:-1].split('],[')
    for line in lines:
        matrix_sizes.append(list(map(int, line.split(','))))

    result = solution(matrix_sizes)
    print(result)
