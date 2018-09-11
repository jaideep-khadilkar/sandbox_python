
from itertools import permutations
input_list = raw_input().split()
string, k = input_list[0], int(input_list[1])
string = sorted(string)
for p in list(permutations(string, k)):
    print ''.join(p)
