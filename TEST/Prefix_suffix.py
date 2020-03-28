import os
import sys

def go_right(s, j):
    while j != len(s)-1 and s[len(s)-1] != s[j]: j += 1
    return j
def go_left(s, j):
    while j != 0 and s[0] != s[j]: j -= 1
    return j

def case2(s):

def case1(s):
    prefix = ''; suffix = ''
    j = len(s) - 1; i = 0;
    while j > 0:
        j = go_left(s, j)
        while i <= j:
            if s[i] != s[j]:break
            prefix = prefix + s[i]
            if i == j: continue
            suffix = s[i] + suffix
        else: return res
        i = 0; prefix = ''; suffix = '';
    return prefix + suffix

def case(s):

    i = 0; prefix = ''; suffix = '';
    while i < (len(s)//2 + len(s)%2) and s[i] == s[len(s)- 1 - i]:
        prefix = prefix + s[i]; i += 1;
        if i == len(s) - 1 - i : break
        suffix = s[i] + suffix

    if i != len(s)-1 - i:
        ans1 = case1(s[i:len(s)-i]); ans2 = case2(s[i:len(s)-i])
        ans = ans1 if len(ans1) >= len(ans2) else ans2

    return prefix + ans + suffix




def solve(s):
    # Divde case by case and compare the values

    # case1: prefix is palindrom
    # case2: suffix is palindrom
    # case3: front and back is same
    res = case(s, res)
    #speical case
    if len(res) == 0:
        return s[0]

if __name__ == '__main__':
    t = int(input())
    for iter_t in range(t):
        s = str(input())
        result = solve(s)
        print(result)
