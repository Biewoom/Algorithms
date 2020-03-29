import sys
import os


def solution(s):
    # strategy and complete-search
    s = s.rstrip("\n")
    ans = len(s)

    for cut in range(1, len(s)//2+1):
        cut_str = s[0:cut]; llist = [[1, cut_str]];new_ans = 0
        for i in range(cut, len(s), cut):

            if i+cut > len(s): llist.append([1, s[i:]]); break
            if cut_str == s[i:i+cut]: llist[-1][0] += 1
            else: llist.append( [1, s[i:i+cut]])
            cut_str = s[i:i+cut]

        for e, v in llist:
            if e != 1: new_ans += len(str(e))
            new_ans += len(v)

        ans = min(ans, new_ans)

    return ans
if __name__ == '__main__':

    for line in sys.stdin:
        if line == '': break
        result = solution(line)
        print(result)
