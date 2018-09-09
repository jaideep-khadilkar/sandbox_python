
from collections import OrderedDict
N = int(raw_input())
L = []
for _ in range(N):
    L.append(raw_input())

d = OrderedDict()
for word in L:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print len(d.keys())
for word in d.keys():
    print d[word],
