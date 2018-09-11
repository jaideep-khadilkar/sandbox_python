
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict
d = defaultdict(list)
N, M = map(int, raw_input().split())
for index in range(1, N+1):
    word = raw_input()
    d[word].append(index)
for _ in range(M):
    word = raw_input()
    if word in d:
        print ' '.join(map(str, d[word]))
    else:
        print -1
