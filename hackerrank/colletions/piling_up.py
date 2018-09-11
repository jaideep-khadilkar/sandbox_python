
# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque
import sys


def test():
    top = sys.maxint
    n = int(raw_input())
    d = deque()
    d.extend(map(int, raw_input().split()))
    while len(d) != 0:
        if d[0] >= d[-1]:
            if d[0] <= top:
                top = d[0]
                d.popleft()
                continue
            else:
                print 'No'
                return
        else:
            if d[-1] <= top:
                top = d[-1]
                d.pop()
                continue
            else:
                print 'No'
                return
    print 'Yes'
    return


T = int(raw_input())
for _ in range(T):
    test()
