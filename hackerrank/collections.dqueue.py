
# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
N = int(raw_input())
d = deque()
for _ in range(N):
    input_list = raw_input().split()
    if input_list[0] == 'append':
        d.append(input_list[1])
    if input_list[0] == 'appendleft':
        d.appendleft(input_list[1])
    if input_list[0] == 'pop':
        d.pop()
    if input_list[0] == 'popleft':
        d.popleft()

print ' '.join(d)
