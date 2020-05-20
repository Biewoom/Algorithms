import os
import sys

def solution(n, words):
    users = [0]*n
    preWord = None
    wordSet = set()

    for i, word in enumerate(words):
        # deternmin users
        u = i%n; users[u] += 1
        if word in wordSet: return [u+1, users[u]]
        if preWord and preWord[-1] != word[0]: return [u+1, users[u]]
        preWord = word
        wordSet.add(word)

    return [0, 0]

if __name__ == '__main__':
    n = int(input())
    words = []
    lines = input()[1:-1].split(',')
    for line in lines:
        words.append(line[1:-1])

    result = solution(n, words)
    print(result)
