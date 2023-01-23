import sys

N = 10
ret = 0
ans = 0
for i in range(N):
    x, y = map(int, sys.stdin.readline().split(' '))
    ret += (y - x)
    ans = max(ans, ret)
print(ans)
