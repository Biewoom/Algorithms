import os
import sys

def solution(n):
    if n%2: return 0
    if n == 0: return 0

    M = 1000000007
    Value = 1
    sum = 0
    n //= 2

    for iter in range(0, n):
        preValue = Value
        Value = ( (Value*3)%M + (2*sum)%M ) % M
        sum = (sum%M + preValue%M)%M
    
    return Value

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)
