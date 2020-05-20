import os
import sys

def solution(s):
    stack = []
    for _s in s:
        if stack and stack[-1] == _s: stack.pop(-1)
        else: stack.append(_s) 

    return 1 if len(stack) == 0 else 0

if __name__ == '__main__':
    s = input()
    result = solution(s)
    print(result)
