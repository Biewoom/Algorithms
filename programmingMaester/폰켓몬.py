import os
import sys

def solution(nums):
    i = 0;
    budget = len(nums)//2
    pocket = set()

    while i < budget and nums:
        pocketMon = nums.pop(0)
        if pocketMon in pocket: continue
        else: i += 1; pocket.add(pocketMon)

    return len(pocket)

if __name__ == '__main__':
    nums = list(map(int, input().split(',') ) )
    result = solution(nums)
    print(result)
