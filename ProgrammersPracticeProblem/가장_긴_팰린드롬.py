import os
import sys

def solution(s):
    answer = 0
    visited = {}

    for startIndex in range(0, len(s)):

        for endIndex in range(startIndex, len(s)):
            length = endIndex - startIndex + 1
            if length < answer: continue
            odd = length%2
            si, ei = startIndex, endIndex
            new = 0

            if odd:
                while si != ei and s[si] == s[ei]:
                    new += 2
                    si += 1; ei -= 1

                if si == ei: answer = max(answer, new+1)

            else:

                while si < ei and s[si] == s[ei]:
                    new += 2
                    si += 1; ei -= 1

                if si > ei: answer = max(answer, new)

    return answer

if __name__ == '__main__':
    s = input()
    result = solution(s)
    print(result)
