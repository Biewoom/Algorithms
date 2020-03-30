import os
import sys

def recur(p):
    if p == "": return ""
    else:
        Sum = 1 if p[0] == '(' else -1
        for i in range(1, len(p)):
            if p[i] == '(': Sum += 1
            else: Sum -= 1

            if Sum == 0: break

        u = p[:i+1]; v = p[i+1:]

        Q = []; balanced = True
        for i in range(0, len(u)):
            if u[i] == ')':
                if not Q:  balanced = False; break
                if Q[-1] == ')': balanced = False; break
                Q.pop()
            else: Q.append(u[i])

        if balanced:
            return u + recur(v)

        else:
            left_u = '(' + recur(v) + ')'
            for _ in u[1:-1]:
                if _ == '(': left_u += ')'
                elif _ == ')': left_u += '('
                else: continue

            return left_u


def solution(p):
    result = recur(p)
    return result

if __name__ == '__main__':

    for line in sys.stdin:
        line = line.rstrip("\n")
        result = solution(line)
        print(result)
