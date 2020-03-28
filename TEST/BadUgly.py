
def BadUgly(N):
    if N == 1: return -1
    elif N == 2: return 43
    else:
        pre_fix = ''; N-= 2
        if N&1: pre_fix += '4'; N-=1;
        pre_fix += '54'*(N//2)
        return pre_fix + '43'


if __name__ == '__main__':
    t = int(input())

    for iter_t in range(t):
        _input = int(input())
        result = BadUgly(_input)
        print(result)
