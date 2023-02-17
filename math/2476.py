import sys

N = int(sys.stdin.readline())
ret = 0
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    if x == y == z:
        ret = max(ret, 10000 + x * 1000)
    elif x == y or x == z:
        ret = max(ret, 1000 + x * 100)
    elif y == z:
        ret = max(ret, 1000 + y * 100)
    else:
        ret = max(ret, max(x, y, z) * 100)
print(ret)
