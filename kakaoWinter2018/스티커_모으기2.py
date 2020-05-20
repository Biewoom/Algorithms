import os
import sys

def solution(sticker):
    # control coner-cases
    if len(sticker) <= 3: return max(sticker)

    # [ (0: o, n-1: o), (0: o, n-1: x ), (0:x, n-1:o), (0:x, n-1:x) ]
    preCases = [sticker[0]+sticker[2], sticker[0], sticker[2], sticker[1]]

    for i in range(3, len(sticker) - 1):
        nextCase1 = preCases[1] + sticker[i]
        nextCase2 = max(preCases[0], preCases[1])
        nextCase3 = preCases[3] + sticker[i]
        nextCase4 = max(preCases[2], preCases[3])

        preCases = [nextCase1, nextCase2, nextCase3, nextCase4]

    # last step
    case1 = preCases[0]; case2 = preCases[1]
    case3 = preCases[2]; case4 = preCases[3] + sticker[len(sticker)-1]
    return max(case1, case2, case3, case4)



if __name__ == '__main__':
    sticker = list( map(int, input().split(',') ) )
    result = solution(sticker)
    print(result)
