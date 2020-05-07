import os
import sys

import re
from collections import defaultdict

def FindIntersection(Dict1, Dict2)->int:
    result = 0
    for key in Dict1:
        if key in Dict2:
            result += min(Dict1[key], Dict2[key])
    return result

def FindUnion(Dict1, Dict2)->int:
    result = 0
    for key in Dict1:
        if key in Dict2:
            result += max(Dict1[key], Dict2[key])
        else:
            result += Dict1[key]
    for key in Dict2:
        if key in Dict1:
            pass
        else:
            result += Dict2[key]

    return result

def StrToDict(str1)->dict:
    Dict = defaultdict(int)
    p = re.compile('[a-zA-Z]+')
    for i in range(0, len(str1) - 1):
        cur_pattern = str1[i:i+2]
        M = p.match(cur_pattern)
        if M and len(M[0]) == len(cur_pattern): Dict[cur_pattern.lower()] += 1
    return Dict

def solution(str1, str2):
    Dict1 = StrToDict(str1)
    Dict2 = StrToDict(str2)

    numerator = FindIntersection(Dict1, Dict2)
    denominator = FindUnion(Dict1, Dict2)
    result = 1 if denominator == 0 else numerator/denominator
    result = int(result*65536)
    return result

if __name__ == '__main__':
    str1 = input()
    str2 = input()
    result = solution(str1, str2)
    print(result)
