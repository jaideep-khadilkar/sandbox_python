
from itertools import combinations
input_list = raw_input().split()
string, k = input_list[0], int(input_list[1])
string = sorted(string)
for r in range(1, k+1):
    for p in list(combinations(string, r)):
        print ''.join(p)
