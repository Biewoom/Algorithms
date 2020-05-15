import os
import sys

def solution(s):
    answer = ''
    Min = sys.maxsize; Max = sys.maxsize*-1

    for _s in s.split(' '):
        num = int(_s)

        Min = min(Min, num)
        Max = max(Max, num)

    answer += "%d"%(Min)
    answer += " "
    answer += "%d"%(Max)

    return answer

if __name__ == '__main__':
    s = input()
    result = solution(s)
    print(result)
