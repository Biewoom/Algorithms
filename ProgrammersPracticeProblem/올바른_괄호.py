import os
import sys

def solution(s):
    stack = []
    for _s in s:
        if _s == '(': stack.append(_s)
        else:
            if stack and stack[-1] == '(': stack.pop(-1)
            else: return False

    if stack: return False
    else: return True

if __name__ == '__main__':
    s = input()
    result = solution(s)
    print(result)
