import sys

x, y = map(int, sys.stdin.readline().split())
ret = str(x // y) + "."

for i in range(0, 1000):
    x = x % y * 10
    ret += str(x // y)

print(ret)
