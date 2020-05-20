import os
import sys

def solution(n, s):
    answer = []
    if n > s: return [-1]

    p, q = divmod(s, n)
    for i in range(n):
        if i < q: answer.append( p + 1 )
        else: answer.append(p)

    answer.sort()
    return answer


if __name__ == '__main__':
    n = int(input())
    s = int(input())
    result = solution(n, s)
    print(result)
