import os
import sys
import re

def parsingHelp(str1):
    num = bonus = op = None
    tempList = list(str1)
    integers = [str(i) for i in range(0, 10)]
    bonuses = ['S', 'D', 'T']
    ops = ['*', '#']

    while tempList:
        if tempList[0] == '1' and tempList[1] == '0':
            num = 10; tempList.pop(0)
        elif tempList[0] in integers:
            num = int(tempList[0])
        elif tempList[0] in bonuses:
            if tempList[0] == 'S': bonus = 1
            elif tempList[0] == 'D': bonus = 2
            else: bonus = 3
        elif tempList[0] in ops:
            op = tempList[0]
        else:
            print("Impossible")
        tempList.pop(0)

    if op:
        return (num, bonus, op)
    else:
        return (num, bonus, '.')

def parsing(dartResult):
    integers = [str(i) for i in range(1, 10)]
    strList = []; dartList = []
    curStr = dartList[0]

    for dart in dartResult[1:]:
        if dart in integers:
            strList.append(curStr)
            curStr = dart
        elif dart == '0':
            if curStr[-1] == '1':
                curStr += dart
            else:
                strList.append(curStr)
                curStr = dart
        else:
            curStr += dart
    strList.append(curStr)
    for str1 in strList:
        dartList.append(parsingHelp(str1))

    return dartList

def solution(dartResult):
    answer = preScore = curScore = 0
    scores = parsing(dartResult)
    # return
    for score in scores:
        curScore = score[0]**score[1]
        if score[2] == '.':
            pass
        elif score[2] == '#':
            curScore *= -1
        elif score[2] == '*':
            curScore *= 2
            preScore *= 2
        else:
            print("Impossible!")

        answer += preScore
        preScore = curScore

    answer += curScore
    return answer

if __name__ == '__main__':
    dartResult = input()
    result = solution(dartResult)
    print(result)
