import os
import sys

result = 0
def recur(left, right, stack):
    global result
    if left == 0 and right == 0: result += 1; return
    if left: recur(left-1, right, stack+1)
    if stack and right: recur(left, right-1, stack-1)

def solution(n):
    global result
    recur(n, n, 0)
    return result

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)
