
from itertools import combinations_with_replacement
input_list = raw_input().split()
string, k = input_list[0], int(input_list[1])
string = sorted(string)
for p in list(combinations_with_replacement(string, k)):
    print ''.join(p)
