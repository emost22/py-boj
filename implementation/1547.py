import sys

N = int(sys.stdin.readline())

ret = 1
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x == ret:
        ret = y
    elif y == ret:
        ret = x
print(ret)
