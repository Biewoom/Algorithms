import os
import sys

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        while word:
            w = word[0]
            if w in cur: cur[w][1] += 1
            else: cur[w] = [{}, 1]
            cur = cur[w][0]
            word = word[1:]

    def search(self, word):
        cur = self.root; result = 0
        while word:
            result += 1
            w = word[0]
            if cur[w][1] == 1: break
            else: cur = cur[w][0]
            word = word[1:]
        return result

def solution(words):
    trie = Trie()
    answer = 0
    # insert
    for word in words:
        trie.insert(word)
    # search
    for word in words:
        answer += trie.search(word)

    return answer


if __name__ == '__main__':
    lines = input().split(',')
    words = []
    for line in lines:
        words.append(line[1:-1])

    result = solution(words)
    print(result)
