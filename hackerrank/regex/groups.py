
# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

S = raw_input()
m = re.search(r'([a-zA-Z0-9])\1',S)
if m:
    print m.groups()[0]
else:
    print -1