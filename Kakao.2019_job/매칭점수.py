import os
import sys
import re

def ParsingName(page, i, Map):
    p = re.compile('<meta property="og:url" content="(.+?)"/>')
    M = p.findall(page)
    Map[M[0]] = i

def ParsingBasic(page, i, word, basic_nodes):
    p = re.compile('[a-zA-Z]+')
    w_list = p.findall(page)
    for w in w_list:
        if word.lower() == w.lower():
            basic_nodes[i] += 1

def ParsingRelation(page, i, Map, edge_count, edgeList):
    p = re.compile('<a href="(.+?)">')
    site_list = p.findall(page)
    for site in site_list:
        if site in Map:
            index = Map[site]
            edgeList[i].append(index)
        edge_count[i] += 1

def solution(word, pages):
    nameMap = dict()
    basic_nodes = [0]*len(pages); final_nodes = [0]*len(pages); edge_count = [0]*len(pages)
    edgeList = [[] for i in range(len(pages))]

    for i, page in enumerate(pages):
        ParsingName(page, i, nameMap)
        ParsingBasic(page, i, word, basic_nodes)

    for i, page in enumerate(pages):
        ParsingRelation(page, i, nameMap, edge_count, edgeList)

    for i, page in enumerate(pages):
        for node in edgeList[i]:
            final_nodes[node] += (basic_nodes[i]/edge_count[i])
        final_nodes[i] += basic_nodes[i]

    Max = result = -1
    for i, final in enumerate(final_nodes):
        if Max < final:
            Max = final
            result = i

    return result

if __name__ == "__main__":
    word = input()
    pages = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        pages.append(line)
    result = solution(word, pages)
    print(result)
