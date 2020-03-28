import os
import sys
import re


from collections import defaultdict
def solve(n, m, llist):

    Dict = defaultdict(int); Max = 0

    for i in range(n):
        for j in range(i+1, n):
            b = "{:b}".format(llist[i]|llist[j])
            d = list(b).count('1')
            Dict[d] += 1
            Max = max(Max, d)

    print(Max)
    print(Dict[Max])


if __name__ == '__main__':
    n, m = map(int, input().split())
    llist = []
    for iter in range(n):
        llist.append( int(input(), 2) )
    solve(n, m , llist)
