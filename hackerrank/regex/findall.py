
# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

S = raw_input()

f = re.findall(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,101}(?=[^aeiouAEIOU])',S)
if len(f):
    for m in f:
        print m
else:
    print -1
