#!/bin/python3

import os
import sys
import re

class Trie:

    def __init__(self):
        self.root = dict()

    def insert(self, s)->int:
        # insert and add it to result
        cur_node = self.root
        Set = set(); res = L = 0; M = round(1e9+7)
        while s:
            Set.add(s[0]); L += 1
            if s[0] not in cur_node:
                res += pow(L, len(Set), M) #add
                cur_node[s[0]] = dict()
            cur_node = cur_node[s[0]]
            s = s[1:]

        return res%M

def superFunctionalStrings(s):

    result = 0; M = round(1e9+7)
    trie = Trie()

    while s:
        result += trie.insert(s)
        s = s[1:]

    return result%M

if __name__ == '__main__':
    t = int(input())
    sys.setrecursionlimit(10**5)

    for t_itr in range(t):
        s = input()

        result = superFunctionalStrings(s)

        print(result)
