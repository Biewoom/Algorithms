import os
import sys

def solution(n):
    binNum = bin(n)[2:]

    for i in range(len(binNum)-1, -1, -1):
        if binNum[i] == '1':
            if i == 0: newNum = binNum + '0'
            else:
                while i > 0 and binNum[i-1] == '1': i -= 1

                if i == 0: newNum = '1' + '0' + binNum[1:][::-1]
                else:
                    newNum = binNum[:i-1] + '10' + binNum[i+1:][::-1]

            break

    return int(newNum,2)

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)
