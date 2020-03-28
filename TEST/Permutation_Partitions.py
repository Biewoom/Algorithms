import os
import sys
M = 998244353

def Partitions(n, k, llist):
    global M
    ans1 = 0; ans2 = 1;
    Set = set(); res = []
    for i in range(k): ans1 += n - i; Set.add(n-i);
    # find ans2
    for i in range(len(llist)):
        if llist[i] in Set: res.append(i)

    for j in range(0, len(res)-1):
        ans2 *= (res[j+1]- res[j])%M

    return [ans1, ans2%M]

if __name__ == '__main__':
    n, k = tuple(map(int, input().split()))
    llist = list( map(int, input().split()) )
    result = Partitions(n, k, llist)
    print(*result)
