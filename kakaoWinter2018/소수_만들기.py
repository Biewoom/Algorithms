import os
import sys

result = 0

def pickNums(i, pickLeft, sum, sieve, nums):
    global result

    if pickLeft == 0:
        if sieve[sum]: result += 1
        return
    elif i >= len(nums): return
    else:
        pickNums(i+1, pickLeft-1, sum+nums[i], sieve, nums)
        pickNums(i+1, pickLeft, sum, sieve, nums)

def sieveOfEratosthenes(sieve):
    sieve[0] = sieve[1] = False
    for num in range(len(sieve)):
        if sieve[num] == -1:
            curNum = num
            while curNum < len(sieve):
                sieve[curNum] = False
                curNum += num
            sieve[num] = True

def solution(nums):
    global result
    sieve = [-1]*3000
    sieveOfEratosthenes(sieve)
    pickNums(0, 3, 0, sieve, nums)
    return result

if __name__ == '__main__':
    nums = list(map(int, input().split(',')))
    result = solution(nums)
    print(result)
