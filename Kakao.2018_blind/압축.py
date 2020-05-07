import os
import sys

def solution(msg):
    Map = {}; answer = []; index = 1
    for i in range(65, 65+26):
        alph = chr(i)
        Map[alph] = index
        index += 1

    while msg:
        curMsg = msg[0]
        msg = msg[1:]
        while msg and curMsg + msg[0] in Map:
            curMsg += msg[0]; msg = msg[1:]

        # print("curMsg: ", curMsg)
        answer.append( Map[curMsg] )
        if msg:
            Map[ curMsg + msg[0] ] = index
            index += 1
    return answer

if __name__ == '__main__':
    msg = input()
    result = solution(msg)
    print(result)
