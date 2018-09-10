
from collections import OrderedDict
N = int(raw_input())
ord_dict = OrderedDict()
for _ in range(N):
    input_str = raw_input()
    input_list = input_str.rsplit(' ', 1)
    item = input_list[0]
    price = input_list[1]
    if item in ord_dict:
        ord_dict[item] += int(price)
    else:
        ord_dict[item] = int(price)

for key in ord_dict:
    print '{0} {1}'.format(key, ord_dict[key])
