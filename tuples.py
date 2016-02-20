from __builtin__ import hash

n = int(raw_input())

for x in range(n-1):
    num = raw_input().strip().split(" ")
    for i in range(len(num)):
        num[i] = int(num[i])

T = tuple(num)

print hash(T)
