#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    Q = []; Set = set()

    for i in range(len(s)):
        if Q and Q[-1] == s[i]:
            Q.pop()
        else:
            Q.append( s[i] )
            
    return "".join(Q) if len(Q) else 'Empty String'


if __name__ == '__main__':
    s = input()

    result = superReducedString(s)

    print(result)
