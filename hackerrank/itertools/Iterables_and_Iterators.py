
from itertools import combinations
N = int(raw_input())
L = raw_input().split()
K = int(raw_input())
C = list(combinations(L, K))
cnt = sum(1 for c in C if 'a' in c)
print (float(cnt)/len(C))
