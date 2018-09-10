
from collections import Counter

X = int(raw_input())
L = map(int, raw_input().split())
cnt = Counter(L)
N = int(raw_input())
profit = 0
for _ in range(N):
    size, amount = map(int, raw_input().split())
    if (size in cnt.keys()) and (cnt[size]>0):
        profit += amount
        cnt[size] -= 1

print profit
