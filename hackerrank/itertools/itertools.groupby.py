
from itertools import groupby
string = raw_input()
groups = groupby(string)
for lable, group in groups:
    print (sum(1 for _ in group), int(lable)),
