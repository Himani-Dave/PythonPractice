n = int(raw_input())

numbers = raw_input().split()
numbers = list(map(int, numbers))

big = 0

for each in numbers:
    if each > big:
        big = each
print big
numbers.remove(big)

for each in numbers:
    if each == big:
        numbers.remove(each)
print numbers
sec = 0
for each in numbers:
    if each > sec:
        sec = each
print sec
