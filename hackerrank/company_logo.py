
# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter
S = raw_input()
cnt = Counter(S)
common_list = cnt.most_common(3)
common_list.sort(key=lambda l: (l[1], ord('z')-ord(l[0])), reverse=True)
for char, count in common_list:
    print '{0} {1}'.format(char, count)
