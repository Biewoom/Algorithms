import os
import sys

def parsing(file):
    integers = [str(i) for i in range(0, 10)]
    start = end = False
    head = ""; number = ""

    for f in file:
        if end: break
        if f in integers:
            start = True
            number += f
        else:
            if start: end = True
            else: head += f

    return head, int(number)

def solution(files):
    temp = []; answer = []
    # x = (head, number, index)
    for i, file in enumerate(files):
        head, number = parsing(file)
        temp.append( (head, number, i))
    # print('temp before sort: ', temp)
    temp.sort(key = lambda x: (x[0].lower(), x[1], x[2]))

    for t in temp:
        answer.append(files[t[2]])
    return answer

if __name__ == '__main__':
    lines = input().split(',')
    files = []
    for line in lines:
        files.append(line[1:-1])

    result = solution(files)
    print(result)
