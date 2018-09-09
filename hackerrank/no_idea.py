
N, M = map(int, raw_input().split())
array = map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))

happiness = 0

for i in array:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print happiness
