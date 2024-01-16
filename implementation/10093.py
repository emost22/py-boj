import sys

l, r = map(int, sys.stdin.readline().split())

if l > r:
    tmp = r
    r = l
    l = tmp

print(max(r - l - 1, 0))
for i in range(l + 1, r):
    print(i, end=' ')
